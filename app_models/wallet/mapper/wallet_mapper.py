import json
import urllib.parse
import urllib.request

from app_models.wallet.mapper.wallet_mapper_interface import WalletMapperInterface
from app_models.wallet.wallet import Wallet
from app_models.wallet.walletDto import WalletDto


def _get_exchanged_wallet(wallet: Wallet) -> WalletDto:
    with urllib.request.urlopen("https://bitpay.com/api/rates") as response:
        response_text = response.read()

    currency_rates = json.loads(response_text)
    btc_to_usd: float = currency_rates[2]["rate"]
    balance_usd = wallet.balance * btc_to_usd
    return WalletDto(wallet.address, wallet.balance, balance_usd)


class WalletMapper(WalletMapperInterface):
    def wallet_to_dto(self, wallet: Wallet) -> WalletDto:
        wallet_dto: WalletDto = _get_exchanged_wallet(wallet)
        return wallet_dto
