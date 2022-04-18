from app_impl.wallet.address_generator import AddressGenerator
from app_models.user.user import User
from app_models.wallet.mapper.wallet_mapper import WalletMapper
from app_models.wallet.wallet import Wallet
from app_models.wallet.walletDto import WalletDto


class TestWalletMapper:
    def test_wallet_mapper_wallet_to_wallet_dto(self) -> None:
        wallet_mapper: WalletMapper = WalletMapper()
        user: User = User(1, "key", False)
        wallet_address_generator: AddressGenerator = AddressGenerator()
        address: str = wallet_address_generator.get_address(user.user_id)
        wallet: Wallet = Wallet(address, user.user_id, 1)
        wallet_dto: WalletDto = wallet_mapper.wallet_to_dto(wallet)
        assert wallet.address == wallet_dto.address
        assert wallet.balance == wallet_dto.balance_in_btc
