from app_impl.wallet.address_generator import AddressGenerator
from app_models.user.user import User
from app_models.wallet.walletDto import WalletDto


class TestWalletDTO:
    def test_wallet_dto(self) -> None:
        user: User = User(1, "key", False)
        wallet_address_generator: AddressGenerator = AddressGenerator()
        address: str = wallet_address_generator.get_address(user.user_id)
        wallet_dto: WalletDto = WalletDto(address, 1, 43000)
        assert address == wallet_dto.address
        assert wallet_dto.balance_in_btc == 1
        assert wallet_dto.balance_in_usd == 43000
