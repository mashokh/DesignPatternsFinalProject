from app_impl.user.user_generator import UserGenerator


class TestUserGenerator:
    def test_user_generator(self) -> None:
        user_generator: UserGenerator = UserGenerator()
        assert user_generator.generate_user_key() != user_generator.generate_user_key()
