from app_impl.wallet.address_generator import AddressGenerator
from app_models.user.user import User


class TestAddressGenerator:
    def test_address_generator(self) -> None:
        user: User = User(1, "key", False)
        wallet_address_generator: AddressGenerator = AddressGenerator()
        assert wallet_address_generator.get_address(
            user.user_id
        ) != wallet_address_generator.get_address(user.user_id)
