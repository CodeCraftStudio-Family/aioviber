from pydantic import BaseModel


class ViberObject(BaseModel):
    event: str
    timestamp: int
    chat_hostname: str
    silent: bool = False
    message_token: int = None

    class Config:
        arbitrary_types_allowed = True
