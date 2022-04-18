import sqlite3
from typing import List, Tuple

from app_db.transaction.transaction_db_interface import TransactionDBInterface
from app_models.transaction.transaction import Transaction

DB_ADDRESS_TRANSACTION: str = "transactions"


class TransactionDB(TransactionDBInterface):
    def __init__(self) -> None:
        self.con_transactions = sqlite3.connect(
            DB_ADDRESS_TRANSACTION, check_same_thread=False
        )
        self.cur_transactions = self.con_transactions.cursor()
        self.cur_transactions.execute(
            """CREATE TABLE IF NOT EXISTS transactions
                       (address_from VARCHAR , address_to VARCHAR, amount REAL, commission REAL)"""
        )

    def create_transaction(self, transaction: Transaction) -> bool:
        self.cur_transactions.execute(
            "INSERT INTO transactions VALUES (?, ?, ?, ?)",
            (
                transaction.address_from,
                transaction.address_to,
                transaction.amount,
                transaction.commission,
            ),
        )
        self.con_transactions.commit()
        return True

    def get_wallet_transactions(self, address: str) -> List[Transaction]:
        wallet_transactions = self.con_transactions.execute(
            "SELECT * FROM transactions WHERE address_from=? OR address_to=?",
            (
                address,
                address,
            ),
        ).fetchall()
        result_set = []
        for transaction in wallet_transactions:
            address_from, address_to, amount, commission = transaction
            curr_transaction = Transaction()
            curr_transaction.amount = amount
            curr_transaction.address_to = address_to
            curr_transaction.address_from = address_from
            curr_transaction.commission = commission
            result_set.append(curr_transaction)
        return result_set

    def get_all_transactions(
        self,
    ) -> List[Transaction]:
        transactions = self.con_transactions.execute(
            "SELECT * FROM transactions"
        ).fetchall()
        result = []
        for transaction in transactions:
            curr_transaction = Transaction()
            (
                curr_transaction.address_from,
                curr_transaction.address_to,
                curr_transaction.amount,
                curr_transaction.commission,
            ) = transaction
            result.append(curr_transaction)
        return result
