from typing import List, Tuple

from app_models.transaction.transaction_dto import TransactionDTO


class TransactionManagerInterface:

    def create_transaction(self, transaction_dto: TransactionDTO, user_id: int) -> bool:
        pass

    def get_user_transaction(self, user_id: int) -> List[TransactionDTO]:
        pass

    def get_wallet_transaction(
            self, address: str, user_id: int
    ) -> List[TransactionDTO]:
        pass

    def get_all_transaction(self) -> Tuple[int, float]:
        pass
