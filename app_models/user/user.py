
class User:
    user_id: int
    api_key: str
    is_admin: bool

    def __init__(self, user_id: int, api_key: str, is_admin=False):
        self.user_id = user_id
        self.api_key = api_key
        self.is_admin = is_admin
