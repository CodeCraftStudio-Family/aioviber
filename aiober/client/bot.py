
from .session.base import BaseSession
from aiober.methods.base import ViberMethod
from aiober.client.session.request import AiohttpSession


class Bot:
    def __init__(
            self,
            token: str,
            session: BaseSession = None
    ):
        self._token = token
        self.session = session if isinstance(session, BaseSession) else AiohttpSession()
    
    @property
    def token(self):
        return self._token

    async def __call__(self, method: ViberMethod, request_runtime: int = None):

        return await self.session(self, method, timeout=request_runtime)
        
