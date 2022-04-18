from fastapi import HTTPException, status


class WalletExceptionHandler:
    @staticmethod
    def max_wallets_reached() -> Exception:
        return HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Maximum amount of wallets reached.",
        )

    @staticmethod
    def wallet_not_found() -> Exception:
        return HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Wallet not found."
        )

    @staticmethod
    def wallet_access_denied() -> Exception:
        return HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Access to wallet denied.",
        )

    @staticmethod
    def wallet_insufficient_funds() -> Exception:
        return HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Insufficient funds",
        )
