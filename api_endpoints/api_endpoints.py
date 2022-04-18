import json
from typing import List, Tuple

from starlette.requests import Request

from app_impl.core import Core
from app_impl.user.user_exception_handler import UserExceptionHandler
from app_models.transaction.transaction_dto import TransactionDTO
from app_models.wallet.wallet import Wallet
from app_models.wallet.walletDto import WalletDto
from fastapi import FastAPI, APIRouter, Depends
from starlette import status
from starlette.responses import Response

core: Core = Core()

app = FastAPI()

api_endpoints = APIRouter()


def check_request_initiator(request: Request, api_key: str):
    if not core.user_manager.check_user(api_key):
        raise UserExceptionHandler.unauthorized_user()


def check_admin(request: Request, admin_key: str):
    if not core.user_manager.check_admin(admin_key):
        raise UserExceptionHandler.user_not_admin()


@api_endpoints.post("/users")
async def create_user(response: Response) -> json:
    response_user = core.user_manager.add_user()
    response.status_code = status.HTTP_200_OK
    return {"user key": response_user}


@api_endpoints.post("/wallets")
async def create_wallet(
    api_key: str, _: None = Depends(check_request_initiator)
) -> WalletDto:
    user_id = core.user_manager.get_user(api_key).user_id
    request_wallet = Wallet("", user_id, 1)
    response_wallet = core.wallet_manager.add_wallet(request_wallet)
    return core.wallet_mapper.wallet_to_dto(response_wallet)


@api_endpoints.get("/wallets/{address}")
async def get_wallet(
    wallet_address: str, api_key: str, _: None = Depends(check_request_initiator)
) -> WalletDto:
    user_id = core.user_manager.get_user(api_key).user_id
    response_wallet: Wallet = core.wallet_manager.get_wallet(wallet_address)
    return core.wallet_mapper.wallet_to_dto(response_wallet)


@api_endpoints.post("/transactions")
async def create_transaction(
    transaction_dto: TransactionDTO,
    api_key: str,
    response: Response,
    _: None = Depends(check_request_initiator),
) -> None:
    user_id = core.user_manager.get_user(api_key).user_id
    success: bool = core.transaction_manager.create_transaction(
        transaction_dto, user_id
    )
    response.status_code = status.HTTP_200_OK
    if not success:
        response.status_code = status.HTTP_406_NOT_ACCEPTABLE


@api_endpoints.get("/transactions")
async def get_user_transactions(
    api_key: str, response: Response, _: None = Depends(check_request_initiator)
) -> List[TransactionDTO]:
    user_id = core.user_manager.get_user(api_key).user_id
    result: List[TransactionDTO] = core.transaction_manager.get_user_transaction(
        user_id
    )
    response.status_code = status.HTTP_200_OK
    return result


@api_endpoints.get("/wallets/{address}/transactions")
async def get_wallet_transactions(
    address: str,
    api_key: str,
    response: Response,
    _: None = Depends(check_request_initiator),
) -> List[TransactionDTO]:
    user_id = core.user_manager.get_user(api_key).user_id
    result: List[TransactionDTO] = core.transaction_manager.get_wallet_transaction(
        address, user_id
    )
    response.status_code = status.HTTP_200_OK
    return result


@api_endpoints.get("/statistics")
async def get_admin_stats(
    admin_key: str, response: Response, _: None = Depends(check_admin)
) -> Tuple[int, float]:
    result = core.transaction_manager.get_all_transaction()
    response.status_code = status.HTTP_200_OK
    return result
