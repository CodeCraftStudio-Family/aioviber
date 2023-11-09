from typing import Any


class Keyboard:
    type: str = 'keyboard'
    defaultHeight: bool = False
    buttons: list["KeyboardButton"] = []

    def from_dict(self, request_data: dict):
        self.type = request_data['Type']
        self.defaultHeight = request_data['DefaultHeight']
        self.buttons = request_data['Buttons']

        return self

    def to_json(self):
        return {
            "Type":self.type,
            "DefaultHeight":self.defaultHeight,
            "Buttons": [
                button.to_json() for button in self.buttons
            ]
        }


class KeyboardButton:
    action_type: str = None
    action_body: str = None
    text: str
    text_size: str = None

    def __init__(self, *, text: str, text_size: str = None, action_body: str = None, action_type: str = 'reply'):
        self.text = text
        self.text_size = text_size
        self.action_body = action_body
        self.action_type = action_type

    def to_json(self) -> dict[str, Any]:
        return {
            "ActionType": self.action_type,
            "ActionBody": self.action_body,
            "Text": self.text,
            "TextSize": self.text_size
        }