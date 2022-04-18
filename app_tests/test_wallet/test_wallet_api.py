import pytest
from fastapi import HTTPException
from fastapi.testclient import TestClient
from api_endpoints.api_endpoints import api_endpoints

client = TestClient(api_endpoints)


def create_user() -> str:
    resp = client.post("/users")
    api_key_1 = resp.json()["user key"]
    return api_key_1


def test_post_wallet() -> None:
    api_key = create_user()
    resp = client.post(f"/wallets?api_key={api_key}")
    assert resp.status_code == 200
    resp_json = resp.json()
    assert resp_json["balance_in_btc"] > 0
    assert resp_json["balance_in_usd"] > 0

    # check error
    with pytest.raises(HTTPException) as e_info:
        client.post("/wallets?api_key=foo")
    assert e_info.value.status_code == 401


def test_get_wallet() -> None:
    api_key = create_user()
    resp = client.post(f"/wallets?api_key={api_key}")
    wallet_address = resp.json()["address"]
    resp = client.get("/wallets/{wallet}?" + f"wallet_address={wallet_address}&api_key={api_key}")
    assert resp.status_code == 200
    resp_json = resp.json()
    assert resp_json["address"] == wallet_address
    assert resp_json["balance_in_btc"] > 0
    assert resp_json["balance_in_usd"] > 0

    # check errors
    with pytest.raises(HTTPException) as e_info:
        client.get("/wallets/{wallet}?" + f"wallet_address=foo&api_key={api_key}")

    assert e_info.value.status_code == 404

    with pytest.raises(HTTPException) as e_info:
        client.get("/wallets/{wallet}?" + f"wallet_address={wallet_address}&api_key=bar")

    assert e_info.value.status_code == 401


def test_wallet_transactions() -> None:
    api_key = create_user()
    resp = client.post(f"/wallets?api_key={api_key}")
    wallet_address = resp.json()["address"]
    resp = client.get(f"wallets/{wallet_address}/transactions?api_key={api_key}")
    assert resp.status_code == 200

    # check errors

    with pytest.raises(HTTPException) as e_info:
        client.get(f"wallets/{wallet_address}/transactions?api_key=bar")
    assert e_info.value.status_code == 401

