from typing import Any

from . import User
from .base import ViberObject

class ConversationStarted(ViberObject):
    type: str
    context: str
    user: User
    subscribed: bool

    def from_dict(self, request_dict):
        super(ConversationStarted, self).from_dict(request_dict)

        self.type = request_dict['type']
        self.context = request_dict.get('context')
        self.user = User().from_dict(request_dict['user'])
        self.subscribed = request_dict.get('subscribed', False)

        return self