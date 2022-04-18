from app_models.transaction.transaction import Transaction
from app_models.transaction.transaction_dto import TransactionDTO


class TransactionMapperInterface:
    def transaction_dto_to_transaction(
        self, transaction_dto: TransactionDTO, user_id: int
    ) -> Transaction:
        pass

    def transaction_to_transaction_dto(
        self, transaction: Transaction
    ) -> TransactionDTO:
        pass
