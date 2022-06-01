from typing import Mapping

from starlette.requests import Request

from fastapi import FastAPI, APIRouter, Depends

from src.common_libs.utils.logger import logger


app = FastAPI()
api_router = APIRouter()

@api_router.post("/")
def read_root(arg: Mapping[str, str]):
    return {"Hello": "World"}

async def log_json(request: Request):
    request_body = await request.json()
    logger.info(request_body)

# the trick here is including log_json in the dependencies:
app.include_router(api_router, dependencies=[Depends(log_json)])