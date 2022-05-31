from typing import Mapping

from starlette.requests import Request

from fastapi import FastAPI, APIRouter, Depends

app = FastAPI()
api_router = APIRouter()

@api_router.post("/")
def read_root(arg: Mapping[str, str]):
    return {"Hello": "World"}

async def log_json(request: Request):
    print(await request.json())

# the trick here is including log_json in the dependencies:
app.include_router(api_router, dependencies=[Depends(log_json)])