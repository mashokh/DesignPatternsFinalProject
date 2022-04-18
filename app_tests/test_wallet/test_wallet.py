from app_impl.wallet.address_generator import AddressGenerator
from app_models.user.user import User
from app_models.wallet.wallet import Wallet


class TestWallet:
    def test_wallet(self) -> None:
        user: User = User(1, "key", False)
        wallet_address_generator: AddressGenerator = AddressGenerator()
        address: str = wallet_address_generator.get_address(user.user_id)
        wallet: Wallet = Wallet(address, user.user_id, 1)
        assert wallet.address == address
        assert wallet.user_id == user.user_id
        assert wallet.balance == 1
