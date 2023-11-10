from aioviber.types import Message

from .base import BaseFilter

class TextFilter(BaseFilter):
    def __init__(self, text: str = None):
        self.text = text
    
    async def __call__(self, message: Message):
        return message.text == self.text