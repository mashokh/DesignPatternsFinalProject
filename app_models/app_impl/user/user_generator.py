import string
import random

from app_impl.user.user_generator_interface import UserGeneratorInterface


class UserGenerator(UserGeneratorInterface):
    def __init__(self) -> None:
        self.char_num = 12

    def generate_user_key(self) -> str:
        key = "".join(
            random.choice(string.ascii_uppercase + string.digits)
            for _ in range(self.char_num)
        )
        return key
