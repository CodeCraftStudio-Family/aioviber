from typing import Any, TYPE_CHECKING
from .base import ViberObject
from .user import User
from .keyboard import Keyboard
from aiober.client.bot import Bot

if TYPE_CHECKING:
    from ..methods import SendMessage

class Message(ViberObject):
    receiver: str = None
    text: str = None
    type: str
    sender: User
    message_token: int = None
    reply_type: Any = None

    media: str = None
    thumbnail: str = None
    file_name: str = None
    size: int = None
    duration: int = None
    rich_media: Keyboard = None
    keyboard: Keyboard = None

    lat: float = None
    lon: float = None

    sticker_id: int = None

    def model_post_init(self, __context):
        self.sender = User(**__context.get('sender')) if __context else None
        self._bot = __context.get('bot') if __context else None
    
    def answer(self, text: str, keyboard: Keyboard = None):
        from ..methods import SendMessage

        return SendMessage(
            chat_id=self.receiver,
            text=text,
            media=self.media,
            thumbnail=self.media,
            rich_media=self.rich_media,
            keyboard=keyboard.to_json(),
            lat=None,
            lon=None,
            sticker_id=None
        ).as_(self._bot)
    
    def answer_picture(self, text: str, media: Any, keyboard: Keyboard = None):
    #    self._bot.send_messages(
    #        self.user.id,
    #        [PictureMessage(text=text, media=media, keyboard=keyboard)]
    #    )
        ...

    def copy_to(self, chat_id: str):
    #    self._bot.send_messages(
    #        chat_id,
    #        [self.to_viber_object()]
    #    )
        ...