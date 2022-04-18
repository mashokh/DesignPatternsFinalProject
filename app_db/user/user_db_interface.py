from app_models.user.user import User
from interfaces.singleton import Singleton


class UserDbInterface(metaclass=Singleton):
    def add_user(self, user_key: str) -> None:
        pass

    def check_user(self, api_key: str) -> bool:
        pass

    def get_user(self, api_key: str) -> User:
        pass

    def check_admin(self, api_key: str) -> bool:
        pass
