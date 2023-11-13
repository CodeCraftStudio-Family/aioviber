import json
from abc import ABC, abstractmethod
from typing import Any

from aiober.methods.base import Response
from .viber import ViberAPIServer, PRODUCTION

DEFAULT_TIMEOUT: float = 60.0


class BaseSession(ABC):

    def __init__(self):
        self.api: ViberAPIServer = PRODUCTION
        self.timeout = DEFAULT_TIMEOUT
    
    @abstractmethod
    async def make_request(self, bot, timeout: int = None):
        
        pass

    def check_response(self, bot, status_code: int, content: str) -> Response:
        try:
            json_data = json.loads(content)
        except Exception as E:
            raise UnicodeDecodeError("failed to decode object")

        response = Response().model_validate(json_data, context={"bot": bot})

        if 200 < status_code < 220:
            return response
        
        raise RuntimeError(f'status code {status_code}')
