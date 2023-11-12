from typing import Any

from .base import ViberObject

class Seen(ViberObject):
    user_id: str
    udid: Any = None

    def from_dict(self, request_dict):
        super(Seen, self).from_dict(request_dict)

        self.user_id = request_dict["user_id"]
        self.udid = request_dict["udid"]

        return self