from typing import List, Tuple

from app_db.transaction.transaction_db import TransactionDB
from app_impl.transaction.transaction_manager_cosntants import (
    INNER_TRANSACTION_FEE_PERCENT,
    OUTER_TRANSACTION_FEE_PERCENT,
)
from app_impl.transaction.transaction_manager_interface import (
    TransactionManagerInterface,
)
from app_impl.user.user_manager import UserManager
from app_impl.wallet.wallet_manager import WalletManager
from app_models.transaction.mapper.transaction_mapper import TransactionMapper
from app_models.transaction.transaction import Transaction
from app_models.transaction.transaction_dto import TransactionDTO


class TransactionManager(TransactionManagerInterface):
    def __init__(self) -> None:
        self.transaction_db: TransactionDB = TransactionDB()
        self.transaction_mapper: TransactionMapper = TransactionMapper()
        self.wallet_manager = WalletManager()
        self.user_manager = UserManager()

    def create_transaction(self, transaction_dto: TransactionDTO, user_id: int) -> bool:
        transaction: Transaction = (
            self.transaction_mapper.transaction_dto_to_transaction(
                transaction_dto, user_id
            )
        )

        self.wallet_manager.charge(
            address=transaction.address_from, amount=transaction.amount, user_id=user_id
        )
        commission = self.__calculate_transaction_fee(transaction)
        transaction.commission = commission
        self.wallet_manager.add_balance(
            address=transaction.address_to,
            amount=transaction.amount - transaction.commission,
        )

        return self.transaction_db.create_transaction(transaction)

    def get_user_transaction(self, user_id: int) -> List[TransactionDTO]:
        user_transactions = list()
        user_wallets = self.wallet_manager.get_wallets_for_user(user_id)
        for wallet in user_wallets:
            wallet_transactions = self.get_wallet_transaction(wallet.address, user_id)
            for wallet_transaction in wallet_transactions:
                if wallet_transaction not in user_transactions:
                    user_transactions.append(wallet_transaction)
        return user_transactions

    def get_wallet_transaction(
        self, address: str, user_id: int
    ) -> List[TransactionDTO]:
        transaction_list = self.transaction_db.get_wallet_transactions(address)
        return self.transaction_mapper.transaction_list_to_transaction_dto_list(
            transaction_list
        )

    def get_all_transaction(self) -> Tuple[int, float]:
        transactions_list = self.transaction_db.get_all_transactions()
        income = 0
        for transaction in transactions_list:
            income += transaction.commission
        return len(transactions_list), income

    def __calculate_transaction_fee(self, transaction: Transaction) -> int:
        wallet_to = self.wallet_manager.get_wallet(transaction.address_to)
        is_inner_transaction = False
        for wallet in self.wallet_manager.get_wallets_for_user(transaction.user_id):
            if wallet.address == wallet_to.address:
                is_inner_transaction = True
        return (
            transaction.amount * INNER_TRANSACTION_FEE_PERCENT
            if is_inner_transaction
            else transaction.amount * OUTER_TRANSACTION_FEE_PERCENT
        )
