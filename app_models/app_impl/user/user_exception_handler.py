from fastapi import HTTPException, status


class UserExceptionHandler:

    @staticmethod
    def unauthorized_user() -> Exception:
        return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                             detail="key isn't valid")

    @staticmethod
    def user_not_admin() -> Exception:
        return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                             detail="user is not admin")