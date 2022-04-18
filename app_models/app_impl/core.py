from app_impl.user.user_manager import UserManager
from app_impl.user.user_manager_interface import UserManagerInterface
from app_models.wallet.mapper.wallet_mapper import WalletMapper
from app_models.wallet.mapper.wallet_mapper_interface import WalletMapperInterface
from interfaces.singleton import Singleton

from app_impl.transaction.transaction_manager import TransactionManager
from app_impl.wallet.wallet_manager import WalletManager
from app_impl.wallet.wallet_manager_interface import WalletManagerInterface
from app_impl.user.user_manager_interface import UserManagerInterface
from app_impl.transaction.transaction_manager_interface import (
    TransactionManagerInterface,
)


class Core(metaclass=Singleton):
    def __init__(self) -> None:
        self.wallet_manager: WalletManagerInterface = WalletManager()
        self.wallet_mapper: WalletMapperInterface = WalletMapper()
        self.transaction_manager: TransactionManagerInterface = TransactionManager()
        self.user_manager: UserManagerInterface = UserManager()
