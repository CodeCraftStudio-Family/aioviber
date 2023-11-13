from .base import ViberMethod

from ..types import Message, Keyboard
from .methods import SEND_MESSAGE


class SendMessage(ViberMethod[Message]):

    __returing__   = Message
    __api_method__ = SEND_MESSAGE

    receiver: int = None
    type: str = None
    text: str = None
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

    def __init__(
            self,
            receiver: int,
            type: str,
            text: str,
            media: str = None,
            thumbnail: str = None,
            file_name: str = None,
            size: int = None,
            duration: int = None,
            rich_media: Keyboard = None,
            keyboard: Keyboard = None,
            lat: float = None,
            lon: float = None,
            sticker_id: int = None
    ) -> None:
        super().__init__(
            receiver=receiver,
            type=type,
            text=text,
            media=media,
            thumbnail=thumbnail,
            file_name=file_name,
            size=size,
            duration=duration,
            rich_media=rich_media,
            keyboard=keyboard,
            lat=lat,
            lon=lon,
            sticker_id=sticker_id
        )
