
class WalletDto:
    address: str
    balance_in_btc: float
    balance_in_usd: float

    def __init__(self, address, balance_in_btc, balance_in_usd):
        self.address = address
        self.balance_in_btc = balance_in_btc
        self.balance_in_usd = balance_in_usd
