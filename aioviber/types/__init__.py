from viberbot.api.viber_requests import ViberRequest

from .massage import Message
from .user import User
from .keyboard import Keyboard, KeyboardButton

def parse_object(request_data: dict, bot):
    print(request_data.get('event'))
    match request_data.get('event'):
        case 'message':
            return Message(bot).from_dict(request_data)
        