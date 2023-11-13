from aiohttp import ClientSession, TCPConnector, FormData
from typing import TypeVar

from aiober.methods.base import ViberMethod

from .base import BaseSession

T = TypeVar('T')


class AiohttpSession(BaseSession):
    def __init__(self):
        self._session: ClientSession = None
    
    async def create_session(self, token: str) -> ClientSession:
        if self._session is None:
            self._session = ClientSession(
                connector=TCPConnector,
                headers={
                    "X-Viber-Auth-Token": token
                }
            )
        
        return self._session

    async def build_form_data(self, data: dict) -> FormData:
        form_data = FormData()

        for key, value in data.items():
            form_data.add_field(key, value if isinstance(value, (int, str)) else value.dict())
        
        return form_data

    async def make_request(self, bot, method: ViberMethod, timeout: int = None):
        session = await self.create_session(bot.token)

        url = self.api.get_api_url(method.__api_method__)
        form_data = self.build_form_data(method.dict())

        try:
            async with session.post(
                url, data=form_data, timeout=self.timeout if timeout is None else timeout
            ) as resp:
                raw_result = await resp.text()
        except RuntimeError:
            raise RuntimeError()
        except Exception as E:
            raise E
        
        response = self.check_response(bot, resp.status, raw_result)

        return response.status

    async def __call__(self, method: ViberMethod[T], timeout_request: int = None):

        await self.make_request(self, method, timeout_request)

