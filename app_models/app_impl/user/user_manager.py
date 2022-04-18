from app_db.user.user_db import UserDb
from app_db.user.user_db_interface import UserDbInterface
from app_impl.user.user_generator import UserGenerator
from app_impl.user.user_manager_interface import UserManagerInterface
from app_models.user.user import User


class UserManager(UserManagerInterface):
    def __init__(self) -> None:
        self.user_generator: UserGenerator = UserGenerator()
        self.user_db: UserDbInterface = UserDb()

    def add_user(self) -> str:
        user_key: str = self.user_generator.generate_user_key()
        self.user_db.add_user(user_key)
        return user_key

    def check_user(self, api_key: str) -> bool:
        return self.user_db.check_user(api_key)

    def get_user(self, api_key: str) -> User:
        return self.user_db.get_user(api_key)

    def check_admin(self, api_key: str) -> bool:
        return self.user_db.check_admin(api_key)
