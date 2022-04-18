from typing import List
from app_models.wallet.wallet import Wallet
from app_db.wallet.wallet_db_interface import WalletDBInterface


class WalletDB(WalletDBInterface):
    def create_db(self) -> None:
        self.cur.execute(
            """CREATE TABLE IF NOT EXISTS wallets(
                            address text,
                            user_id INTEGER,
                            balance)"""
        )

    def add_wallet(self, wallet: Wallet) -> Wallet:
        self.cur.execute(
            "INSERT INTO wallets VALUES(?, ?, ?)",
            (wallet.address, wallet.user_id, wallet.balance),
        )
        self.con.commit()
        return self.get_wallet(wallet.address)

    def get_wallet(self, address: str) -> Wallet:
        wallet = self.cur.execute(
            "SELECT * FROM wallets WHERE address = ?", (address,)
        ).fetchone()
        address, user_id, balance = wallet
        return Wallet(address, user_id, float(balance))

    def get_wallet_count(self, user_id: int) -> int:
        count = self.cur.execute(
            "SELECT COUNT(*) FROM wallets WHERE user_id = ?", (user_id,)
        ).fetchone()[0]
        if count is None:
            return 0
        return count

    def wallet_exists(self, address: str) -> bool:
        result = self.cur.execute(
            "SELECT * FROM wallets WHERE address = ?", (address,)
        ).fetchone()
        return result is not None

    def change_wallet_balance(self, address: str, new_amount: float):
        self.cur.execute(
            "UPDATE wallets SET balance = ? WHERE address = ?", (new_amount, address)
        )
        self.con.commit()

    def get_user_wallets(self, user_id: int) -> List[Wallet]:
        wallet_list = self.cur.execute(
            "SELECT * FROM wallets WHERE user_id = ?", (user_id,)
        ).fetchall()
        result_set = []
        for wallet in wallet_list:
            address, key, balance = wallet
            result_set.append(Wallet(address, key, balance))
        return result_set if wallet_list is not None else []
