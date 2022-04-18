from typing import List

from app_models.transaction.transaction import Transaction


class TransactionDBInterface:
    def create_transaction(self, transaction: Transaction) -> bool:
        pass

    def get_wallet_transactions(self, address: str) -> List[Transaction]:
        pass

    def get_all_transactions(
        self,
    ) -> List[Transaction]:
        pass
