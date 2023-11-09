

class User:
    id: str = None
    name: str = None
    avatar: str = None
    language: str = 'en'
    country: str = None
    api_version: int = 8

    def from_dict(self, request_data: dict):
        self.id = request_data.get('id')
        self.name = request_data.get('name')
        self.avatar = request_data.get('avatar')
        self.language = request_data.get('language')
        self.country = request_data.get('country')
        self.api_version = request_data.get('api_version')

        return self