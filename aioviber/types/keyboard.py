from typing import Any
from dataclasses import dataclass

class Keyboard:
    type: str = 'keyboard'
    defaultHeight: bool = False
    buttons: list["KeyboardButton"] = []

    def __init__(self, *, buttons: list["KeyboardButton"]):
        self.buttons = buttons

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

@dataclass
class KeyboardButton:
    column: int = 6
    row: int = 1
    bg_color: str = None
    bg_media_type: str = None
    bg_media: str = None
    bg_media_scale_type: str = None
    bg_loop: bool = True
    action_type: str = None
    open_url_type: str = None
    open_url_media_type: str = None
    text_bg_gradient_color: str = None
    text_should_fit: str = None
    internal_browser: Any = None
    Map: Any = None
    image: str = None
    image_scale_type: str = None
    action_body: str = ''
    text_v_align: str = 'middle'
    text_h_align: str = 'center'
    text_padding: list[int] = None
    text: str = None
    text_opacity: int = 100
    text_size: str = 'regular'
    

    def __post_init__(self):
        pass

    def to_json(self) -> dict[str, Any]:
        return {
            "Columns": self.column,
			"Rows": self.row,
			"BgColor": self.bg_color,
			"BgMediaType": self.bg_media_type,
            "BgMediaScaleType": self.bg_media_scale_type,
			"BgMedia": self.bg_media,
			"BgLoop": self.bg_loop,
			"ActionType": self.action_type,
			"ActionBody": self.action_body,
            "OpenURLType": self.open_url_type,
            "OpenURLMediaType": self.open_url_media_type,
			"Image": self.image,
            "ImageScaleType": self.image_scale_type,
			"Text": self.text,
            "TextBgGradientColor": self.text_bg_gradient_color,
            "TextPaddings": self.text_padding,
			"TextVAlign": self.text_v_align,
			"TextHAlign": self.text_h_align,
			"TextOpacity": self.text_opacity,
			"TextSize": self.text_size,
            "TextShouldFit": self.text_should_fit,
            "Map": self.Map
        }
