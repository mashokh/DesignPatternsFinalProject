from pydantic import BaseModel


class TransactionDTO(BaseModel):
    address_from: str
    address_to: str
    amount: float
