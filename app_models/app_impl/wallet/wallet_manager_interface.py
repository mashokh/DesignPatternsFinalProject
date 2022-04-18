from typing import List

from app_models.wallet.wallet import Wallet


class WalletManagerInterface:

    def add_wallet(self, wallet: Wallet) -> Wallet:
        pass

    def get_user_wallet(self, address: str, user_id: int) -> Wallet:
        pass

    def get_wallet(self, address: str) -> Wallet:
        pass

    def charge(self, address: str, amount: float, user_id: int) -> float:
        pass

    def add_balance(self, address: str, amount: float) -> float:
        pass

    def get_wallets_for_user(self, user_id: int) -> List[Wallet]:
        pass
