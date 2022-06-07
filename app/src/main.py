import random
import uuid
from datetime import datetime

from fastapi import Depends, FastAPI, HTTPException
from starlette.middleware.cors import CORSMiddleware

from src.common_libs.middleware import LoggingMiddleware
from src.common_libs.constants.settings import app_settings
from src.common_libs.utils.logging import logger
from src.routers.api import router as api_router

from src.databases.sql_databases.db_config import Base, engine, get_db


Base.metadata.create_all(bind=engine)


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
app.include_router(api_router)

@app.get('/')
async def root():
    logger.info("Root Route")
    return {"detail": "root"}
