from pydantic import parse_obj_as
from .base import ViberObject

from .massage import Message
from .user import User
from .seen import Seen
from .conversation_started import ConversationStarted
from .subscribed import Subscribed, Unsubscribed
from .keyboard import Keyboard, KeyboardButton

_object: dict[str, ViberObject] = {
    'message': Message,
    'seen': Seen,
    'conversation_started': ConversationStarted,
    'subscribed': Subscribed,
    'unsubscribed': Unsubscribed
}

def parse_object(request_data: dict, bot):
    event: str = request_data.get('event')

    kwargs = {'bot': bot} if event == 'message' else {}

    return parse_obj_as(_object[event], request_data | kwargs | request_data[event]) if event in _object else None

