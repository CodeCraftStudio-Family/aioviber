from abc import abstractmethod

class ViberObject:
    event_type: str
    timestamp: int
    chat_hostname: str
    silent: bool
    message_token: int

    @abstractmethod
    def from_dict(self, request_dict):
        """
        Get object by request data
        """
        
        self.event_type = request_dict['event']
        self.timestamp = request_dict['timestamp']
        self.chat_hostname = request_dict.get('chat_hostname')
        self.message_token = request_dict.get('message_token')
        self.silent = request_dict.get('silent')
        
        return self