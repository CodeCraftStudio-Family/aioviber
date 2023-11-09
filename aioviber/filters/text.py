from .base import BaseFilter

class TextFilter(BaseFilter):
    def __init__(self, text: str = None):
        self.text = text