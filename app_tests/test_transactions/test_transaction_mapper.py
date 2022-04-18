from decimal import Decimal

from app_models.transaction.mapper.transaction_mapper import TransactionMapper
from app_models.transaction.transaction import Transaction
from app_models.transaction.transaction_dto import TransactionDTO

transaction_mapper: TransactionMapper = TransactionMapper()


class TestTransactionMapper:
    def test_transaction_mapper_transaction_dto_to_transaction(self) -> None:
        external_data = {
            "address_from": "wallet4",
            "address_to": "wallet5",
            "amount": "12",
        }
        transaction_dto: TransactionDTO = TransactionDTO(**external_data)
        user_id: int = 1

        transaction: Transaction = transaction_mapper.transaction_dto_to_transaction(
            transaction_dto, user_id
        )

        assert transaction.user_id == user_id
        assert transaction.amount == Decimal(12)
        assert transaction.address_from == "wallet4"
        assert transaction.address_to == "wallet5"

    def test_transaction_mapper_transaction_to_transaction_dto(self) -> None:
        transaction: Transaction = Transaction()
        transaction.address_from = "wallet5"
        transaction.address_to = "wallet5"
        transaction.amount = Decimal(11)
        transaction.api_key = "user2"
        transaction.commission = Decimal(1.3)

        transaction_dto: TransactionDTO = (
            transaction_mapper.transaction_to_transaction_dto(transaction)
        )

        assert transaction_dto.amount == Decimal(11)
        assert transaction_dto.address_from == "wallet5"
        assert transaction_dto.address_to == "wallet5"
