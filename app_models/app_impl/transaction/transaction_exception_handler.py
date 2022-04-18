from fastapi import HTTPException, status


class TransactionExceptionHandler:
    @staticmethod
    def user_is_not_admin() -> Exception:
        return HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="This can only be performed by admin.",
        )
