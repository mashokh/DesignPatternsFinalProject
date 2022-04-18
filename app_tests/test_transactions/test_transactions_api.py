import pytest
from fastapi import HTTPException
from fastapi.testclient import TestClient

from api_endpoints.api_endpoints import api_endpoints

client = TestClient(api_endpoints)


def test_post_transaction() -> None:
    api_key_1, api_key_2 = create_users()
    wallet_address_1, wallet_address_2 = create_wallets(api_key_1, api_key_2)
    resp = client.post(f"/transactions?api_key={api_key_1}", json={"address_from": wallet_address_1,
                                                                   "address_to": wallet_address_2,
                                                                   "amount": "1"})
    assert resp.status_code == 200

    # checking errors
    with pytest.raises(HTTPException) as e_info:
        client.post(f"/transactions?api_key=foo", json={"address_from": wallet_address_2,
                                                        "address_to": wallet_address_1,
                                                        "amount": "1"})

    assert e_info.value.status_code == 401

    with pytest.raises(HTTPException) as e_info:
        client.post(f"/transactions?api_key={api_key_2}", json={"address_from": wallet_address_1,
                                                                "address_to": wallet_address_2,
                                                                "amount": "1"})
    assert e_info.value.status_code == 403

    with pytest.raises(HTTPException) as e_info:
        client.post(f"/transactions?api_key={api_key_1}", json={"address_from": wallet_address_1,
                                                                "address_to": wallet_address_2,
                                                                "amount": "100"})
    assert e_info.value.status_code == 400



def test_get_transaction() -> None:
    api_key_1, api_key_2 = create_users()
    wallet_address_1, wallet_address_2 = create_wallets(api_key_1, api_key_2)
    client.post(f"/transactions?api_key={api_key_1}", json={"address_from": wallet_address_1,
                                                            "address_to": wallet_address_2,
                                                            "amount": "1"})
    resp = client.get(f"/transactions?api_key={api_key_1}")
    assert resp.status_code == 200
    assert len(resp.json()) >= 1

    # check errors

    with pytest.raises(HTTPException) as e_info:
        client.get("/transactions?api_key=foo")
    assert e_info.value.status_code == 401


def create_users() -> tuple:
    resp = client.post("/users")
    api_key_1 = resp.json()["user key"]
    resp = client.post("/users")
    api_key_2 = resp.json()["user key"]
    return api_key_1, api_key_2


def create_wallets(user_key_1: str, user_key_2: str) -> tuple:
    resp = client.post(f"/wallets?api_key={user_key_1}")
    wallet_address_1 = resp.json()["address"]
    resp = client.post(f"/wallets?api_key={user_key_2}")
    wallet_address_2 = resp.json()["address"]
    return wallet_address_1, wallet_address_2
