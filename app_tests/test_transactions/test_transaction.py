from decimal import Decimal

from app_models.transaction.transaction import Transaction


class TestTransaction:
    def test_transaction(self) -> None:
        transaction: Transaction = Transaction()
        transaction.address_from = "wallet1"
        transaction.address_to = "wallet2"
        transaction.api_key = "user1"
        transaction.amount = Decimal(22)
        transaction.commission = Decimal(1.2)
        assert transaction.address_from == "wallet1"
        assert transaction.address_to == "wallet2"
        assert transaction.amount == Decimal(22)
        assert transaction.commission == Decimal(1.2)
        assert transaction.api_key == "user1"

    def test_transaction_again(self) -> None:
        transaction: Transaction = Transaction()
        transaction.address_from = "wallet4"
        transaction.address_to = "wallet4"
        transaction.api_key = "user2"
        transaction.amount = Decimal(12)
        transaction.commission = Decimal(0)
        assert transaction.address_from == "wallet4"
        assert transaction.address_to == "wallet4"
        assert transaction.amount == Decimal(12)
        assert transaction.commission == Decimal(0)
        assert transaction.api_key == "user2"
