import sqlite3
from typing import List

from app_models.wallet.wallet import Wallet
from interfaces.singleton import Singleton

DB_ADDRESS: str = "wallet"


class WalletDBInterface(metaclass=Singleton):
    def __init__(self) -> None:
        self.con = sqlite3.connect(DB_ADDRESS, check_same_thread=False)
        self.cur = self.con.cursor()
        self.address = 1

    def create_db(self):
        pass

    def add_wallet(self, wallet: Wallet) -> Wallet:
        pass

    def get_wallet_count(self, user_id: int) -> int:
        pass

    def get_wallet(self, address: str) -> Wallet:
        pass

    def wallet_exists(self, address: str) -> bool:
        pass

    def change_wallet_balance(self, address: str, new_amount: float):
        pass

    def get_user_wallets(self, user_id: int) -> List[Wallet]:
        pass
