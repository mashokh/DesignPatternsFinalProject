from app_models.user.user import User


class UserManagerInterface:
    def add_user(self) -> str:
        pass

    def check_user(self, api_key: str) -> bool:
        pass

    def get_user(self, api_key: str) -> User:
        pass
