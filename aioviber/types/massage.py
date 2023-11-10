from viberbot import Api

from typing import Any

from viberbot.api.messages import (
    TextMessage,
    FileMessage,
    PictureMessage,
    VideoMessage,
    StickerMessage,
    URLMessage,
    RichMediaMessage,
    LocationMessage
)

from .base import ViberObject
from .user import User
from .keyboard import Keyboard


class Message(ViberObject):
    text: str = None
    content_type: str
    user: User
    message_token: str
    chat_id = None
    reply_type = None

    media_url: str = None
    thumbnail_url: str = None
    file_name: str = None
    file_size: int = None
    duration: int = None
    rich_media: Keyboard = None

    lat: float = None
    lon: float = None

    sticker_id: int = None

    def __init__(self, bot: Api):
        self.bot = bot

    def from_dict(self, request_dict: dict) -> "Message":
        message = request_dict.get('message', {})
        super(Message, self).from_dict(request_dict)
        self.content_type = message['type']
        self.user = User().from_dict(request_dict.get('sender', {}))

        match self.content_type: 
            case "text":
                self.text = message['text']
            case "picture":
                self.media_url = message['media']
                self.thumbnail_url = message['thumbnail']
                self.file_name = message['file_name']
                self.file_size = message['size']
            case "file":
                self.media_url = message['media']
                self.file_name = message['file_name']
                self.file_size = message['size']
            case "video":
                self.media_url = message['media']
                self.thumbnail_url = message['thumbnail']
                self.file_size = message['size']
                self.duration = message['duration']
            case 'location':
                self.lat = message['lat']
                self.lon = message['lon']
            case 'url':
                self.media_url = message['media']
            case 'sticker':
                self.sticker_id = message['sticker_id']
            case 'rich_media':
                self.rich_media = message['rich_media']
            case _:
                self.text = message.get('text')
        return self

    def to_json(self) -> dict[str, Any]:
        match self.content_type: 
            case "text":
                return {
                    'type': self.content_type,
                    'text': self.text
                }
            case "picture":
                return {
                    'type': self.content_type,
                    'media': self.media_url,
                    'thumbnail': self.thumbnail_url,
                    'file_name': self.file_name,
                    'size': self.file_size
                }
            case "file":
                return {
                    'type': self.content_type,
                    'media': self.media_url,
                    'file_name': self.file_name,
                    'size': self.file_size
                }
            case "video":
                return {
                    'type': self.content_type,
                    'media': self.media_url,
                    'thumbnail': self.thumbnail_url,
                    'size': self.file_size,
                    'duration': self.duration
                }
            case 'location':
                return {
                    'type': self.content_type,
                    'lat': self.lat,
                    'lon': self.lon
                }
            case 'url':
                return {
                    'type': self.content_type,
                    'media': self.media_url
                }
            case 'sticker':
                return {
                    'type': self.content_type,
                    'sticker_id': self.sticker_id
                }
            case 'rich_media':
                return {
                    'type': self.content_type,
                    'rich_media': self.rich_media.to_json()
                }
            case _:
                return {
                    'type': self.content_type,
                    'text': self.text
                }

    def to_viber_object(self) -> TextMessage | PictureMessage | VideoMessage | FileMessage | URLMessage | RichMediaMessage:
        match self.content_type: 
            case "text":
                return TextMessage(text=self.text)
            case "picture":
                return PictureMessage(
                    text=self.text,
                    media=self.media_url,
                    thumbnail=self.thumbnail_url
                )
            case "file":
                return FileMessage(
                    media=self.media_url,
                    file_name=self.file_name
                )
            case "video":
                return VideoMessage(
                    media=self.media_url,
                    thumbnail=self.thumbnail_url,
                    text=self.text
                )
            case 'location':
                return {
                    'type': self.content_type,
                    'lat': self.lat,
                    'lon': self.lon
                }
            case 'url':
                return URLMessage(
                    media=self.media_url
                )
            case 'sticker':
                return StickerMessage(
                    sticker_id=self.sticker_id
                )
            case 'rich_media':
                return RichMediaMessage(
                    rich_media=self.rich_media.to_json()
                )
            case _:
                return TextMessage(
                    text=self.text
                )

    def answer(self, text: str, keyboard: Keyboard = None):
        self.bot.send_messages(
            self.user.id,
            [TextMessage(text=text, keyboard=keyboard)]
        )
    
    def answer_picture(self, text: str, media: Any, keyboard: Keyboard = None):
        self.bot.send_messages(
            self.user.id,
            [PictureMessage(text=text, media=media, keyboard=keyboard)]
        )
    
    def copy_to(self, chat_id: str):
        self.bot.send_messages(
            chat_id,
            [self.to_viber_object()]
        )

