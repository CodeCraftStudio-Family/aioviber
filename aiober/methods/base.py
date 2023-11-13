from typing import Generic, TypeVar, Any, Generator
from pydantic import BaseModel

from aiober.client.context_controller import BotContextController

ViberType = TypeVar('ViberType', bound=Any)


class Response(BaseModel):
    status: int
    status_message: str
    message_token: int
    chat_hostname: str
    billing_status: int


class ViberMethod(BotContextController, BaseModel, Generic[ViberType]):
    def __init__(self, bot):
        self._bot = bot
    
    async def emit(self, bot) -> ViberType:
        return await bot(self)

    def __await__(self) -> Generator[Any, None, ViberType]:
        if not self._bot:
            raise RuntimeError()
        return self.emit(self._bot).__await__()
