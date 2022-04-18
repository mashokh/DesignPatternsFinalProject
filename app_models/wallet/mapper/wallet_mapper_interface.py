from app_models.wallet.wallet import Wallet
from app_models.wallet.walletDto import WalletDto


class WalletMapperInterface:
    def wallet_to_dto(self, wallet: Wallet) -> WalletDto:
        pass

    def dto_to_wallet(self, wallet_dto: WalletDto) -> Wallet:
        pass
