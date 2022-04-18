import sqlite3

from app_db.user.user_db_interface import UserDbInterface
from app_models.user.user import User
from interfaces.singleton import Singleton

DB_ADDRESS_USERS: str = "users"


def run_once(f):
    def wrapper(*args, **kwargs):
        if not wrapper.has_run:
            wrapper.has_run = True
            return f(*args, **kwargs)

    wrapper.has_run = False
    return wrapper


class UserDb(UserDbInterface):
    def __init__(self) -> None:
        self.con_users = sqlite3.connect(DB_ADDRESS_USERS, check_same_thread=False)
        self.cur_users = self.con_users.cursor()
        self.admin_key = "zxcvb1!"
        self.cur_users.execute(
            """CREATE TABLE IF NOT EXISTS users
                       (userId INTEGER PRIMARY KEY AUTOINCREMENT, key VARCHAR, admin bool)"""
        )
        self.add_admin()

    def add_user(self, user_key: str) -> None:
        self.cur_users.execute(
            "INSERT INTO users(key, admin) VALUES(?, ?)", (user_key, False)
        )
        self.con_users.commit()

    def check_user(self, api_key: str) -> bool:
        user = self.cur_users.execute(
            "SELECT * FROM users WHERE key = ?", (api_key,)
        ).fetchone()
        return user is not None

    def get_user(self, api_key: str) -> User:
        user = self.cur_users.execute(
            "SELECT * FROM users WHERE key = ?", (api_key,)
        ).fetchone()
        user_id, api_key, is_admin = user
        return User(user_id, api_key, is_admin)

    def check_admin(self, api_key: str) -> bool:
        user = self.cur_users.execute(
            "SELECT * FROM users WHERE key = ?", (api_key,)
        ).fetchone()
        if user is not None:
            _, _, is_admin = user
            return is_admin
        else:
            return False

    @run_once
    def add_admin(self):
        self.cur_users.execute(
            "INSERT INTO users(key, admin) VALUES(?, ?)", (self.admin_key, True)
        )
        self.con_users.commit()
