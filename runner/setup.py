from fastapi import FastAPI

from api_endpoints.api_endpoints import api_endpoints


def setup() -> FastAPI:
    app = FastAPI()
    app.include_router(api_endpoints)
    return app
