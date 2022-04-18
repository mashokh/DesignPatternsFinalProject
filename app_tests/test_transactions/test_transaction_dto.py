from decimal import Decimal

from app_models.transaction.transaction_dto import TransactionDTO


class TestTransaction:
    def test_transaction(self) -> None:
        external_data = {
            "address_from": "wallet4",
            "address_to": "wallet5",
            "amount": "12",
        }
        transaction_dto: TransactionDTO = TransactionDTO(**external_data)
        assert transaction_dto.address_from == "wallet4"
        assert transaction_dto.address_to == "wallet5"
        assert transaction_dto.amount == Decimal(12)

    def test_transaction_again(self) -> None:
        external_data = {
            "address_from": "wallet5",
            "address_to": "wallet5",
            "amount": "1",
        }
        transaction_dto: TransactionDTO = TransactionDTO(**external_data)
        assert transaction_dto.address_from == "wallet5"
        assert transaction_dto.address_to == "wallet5"
        assert transaction_dto.amount == Decimal(1)
