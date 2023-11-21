import time
import logging
import asyncio
from contextlib import suppress
from aiohttp import web
from aiohttp.web import Application, Request, Response

from typing import Any

from .router import Router
from aiober.types import Message, parse_object, ViberObject
from aiober.fsm.storage import MemoryStorage, StorageKey
from aiober.fsm.context import FSMcontext
from aiober.client.bot import Bot

events_uses_user = ('conversation_started', 'subscribed')

class Dispatcher(Router):

    def __init__(
            self,
            *,
            bot: Bot,
            storage: Any = None,
            fsm_strategy: Any = None,
            disable_fsm: bool = False,
            name: str = None,
            **kwargs
    ):  
        super(Dispatcher, self).__init__()
        
        self.bot = bot
        self.name = name
        self.storage = (storage or MemoryStorage()) if not disable_fsm else None
        self.kwargs = kwargs
        self.sub_routers = [self]

    async def _listen_webhook(self, request: Request):
        data = await request.json()

        if data.get('event') == 'webhook': return Response()

        #if not self.bot.verify_signature(data_text.encode(), request.headers.get('X-Viber-Content-Signature')):
        #    return Response(status=403)

        #viber_request: ViberRequest = self.bot.parse_request(data_text)

        event: ViberObject = parse_object(data, self.bot)

        start_time = time.time()

        # дописати
        try:
            storage_key = StorageKey(
                user_id=event.user.id if event.event in events_uses_user else event.sender.id,
                chat_id='null'
            )
            state = FSMcontext(storage_key, self.storage)
        except Exception:
            state = None

        handled = await self._trigging(data.get('event'), event, state=state, **self.kwargs)

        now = time.time()
        dif = round(now - start_time, 2)

        logging.info(f"Update in{' not' if not handled else ''} handled - {dif} ms")
        
        return Response(status=200)

    async def _trigging(self, _type: str, *args, **kwargs) -> bool:
        for router in self.sub_routers:
            result = await router.trigger(_type, *args, **kwargs)
            if result: return True

        return False


    async def start_webhook(
            self,
            *,
            app: Application = None,
            host: str = '127.0.0.1',
            port: int = 8000,
            path: str = '/',
            **kwargs: Any
        ):
        app = app if isinstance(app, Application) else Application()

        self.kwargs = kwargs
        app.add_routes([web.post(path, self._listen_webhook)])

        with suppress(asyncio.CancelledError):
            await web._run_app(
                app,
                host=host,
                port=port
            )
