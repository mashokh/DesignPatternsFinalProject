
class Wallet:
    address: str
    user_id: int
    balance: float

    def __init__(self, address, user_id, balance):
        self.address = address
        self.user_id = user_id
        self.balance = balance
