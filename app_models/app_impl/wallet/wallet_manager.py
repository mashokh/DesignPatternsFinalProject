from typing import List

from app_db.wallet.wallet_db import WalletDB
from app_db.wallet.wallet_db_interface import WalletDBInterface
from app_impl.wallet.address_generator import AddressGenerator
from app_impl.wallet.wallet_exception_handler import WalletExceptionHandler
from app_impl.wallet.wallet_manager_interface import WalletManagerInterface
from app_models.wallet.wallet import Wallet
from app_impl.wallet.address_generator_interface import AddressGeneratorInterface


class WalletManager(WalletManagerInterface):
    def __init__(self):
        self.wallet_db: WalletDBInterface = WalletDB()
        self.address_generator: AddressGeneratorInterface = AddressGenerator()
        self.wallet_db.create_db()

    def add_wallet(self, wallet: Wallet) -> Wallet:
        if self.wallet_db.get_wallet_count(wallet.user_id) == 3:
            raise WalletExceptionHandler.max_wallets_reached()
        wallet.address = self.address_generator.get_address(wallet.user_id)
        return self.wallet_db.add_wallet(wallet)

    def get_wallet(self, address: str) -> Wallet:
        if not self.wallet_db.wallet_exists(address):
            raise WalletExceptionHandler.wallet_not_found()
        response_wallet = self.wallet_db.get_wallet(address)
        return response_wallet

    def get_user_wallet(self, address: str, user_id: int) -> Wallet:
        response_wallet = self.get_wallet(address)
        if user_id != "" and response_wallet.user_id != user_id:
            raise WalletExceptionHandler.wallet_access_denied()
        return response_wallet

    def charge(self, address: str, amount: float, user_id: int) -> float:
        wallet = self.get_user_wallet(address, user_id)
        if wallet.balance < amount:
            raise WalletExceptionHandler.wallet_insufficient_funds()
        new_amount = wallet.balance - amount
        self.wallet_db.change_wallet_balance(address, new_amount)
        return new_amount

    def add_balance(self, address: str, amount: float) -> float:
        wallet = self.get_wallet(address)
        new_amount = wallet.balance + amount
        self.wallet_db.change_wallet_balance(address, new_amount)
        return new_amount

    def get_wallets_for_user(self, user_id: int) -> List[Wallet]:
        return self.wallet_db.get_user_wallets(user_id)
