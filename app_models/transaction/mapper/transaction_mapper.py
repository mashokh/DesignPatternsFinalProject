from typing import List

from app_models.transaction.mapper.transaction_mapper_interface import (
    TransactionMapperInterface,
)
from app_models.transaction.transaction import Transaction
from app_models.transaction.transaction_dto import TransactionDTO
from interfaces.singleton import Singleton


class TransactionMapper(TransactionMapperInterface, metaclass=Singleton):
    def transaction_dto_to_transaction(
        self, transaction_dto: TransactionDTO, user_id: int
    ) -> Transaction:
        transaction: Transaction = Transaction()
        transaction.address_from = transaction_dto.address_from
        transaction.address_to = transaction_dto.address_to
        transaction.amount = transaction_dto.amount
        transaction.user_id = user_id
        return transaction

    def transaction_to_transaction_dto(
        self, transaction: Transaction
    ) -> TransactionDTO:
        external_data = {
            "address_from": transaction.address_from,
            "address_to": transaction.address_to,
            "amount": transaction.amount,
        }
        transaction_dto: TransactionDTO = TransactionDTO(**external_data)
        return transaction_dto

    def transaction_list_to_transaction_dto_list(
        self, transaction_list: List[Transaction]
    ) -> List[TransactionDTO]:
        return [
            self.transaction_to_transaction_dto(transaction)
            for transaction in transaction_list
        ]
