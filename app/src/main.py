from typing import Union

import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from starlette.middleware.cors import CORSMiddleware

from src.common_libs.middleware import LoggingMiddleware
from src.common_libs.constants.settings import app_settings
from src.common_libs.utils.logging import logger


def get_application() -> FastAPI:
    application = FastAPI(
        title=app_settings.PROJECT_NAME,
        debug=app_settings.DEBUG,
        version=app_settings.VERSION
    )

    application.add_middleware(
        CORSMiddleware,
        allow_origins=app_settings.ALLOWED_HOSTS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    return application


app = get_application()
app.middleware('http')(
    LoggingMiddleware()
)

class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None

@app.post('/')
async def root():
    logger.info("Got /")
    return {"answer": "I am Root"}


@app.get('/error')
async def error(one: int, two: int):
    """ Example with traceback
    """
    logger.info(f"Got /error, {one=}, {two=}")
    return one / two