from app_models.user.user import User


class TestUser:
    def test_user_model(self) -> None:
        user: User = User(1, "API_KEY_STUB", False)
        assert user.user_id == 1
        assert user.api_key == "API_KEY_STUB"
        assert user.is_admin is False
