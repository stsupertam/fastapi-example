
import uvicorn
from fastapi import FastAPI, HTTPException
from starlette.middleware.cors import CORSMiddleware

from src.common_libs.middleware import LoggingMiddleware
from src.common_libs.constants.settings import app_settings
from src.common_libs.utils.logging import logger
from src.schemas.price_request import PriceRequest

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

@app.get('/')
async def root():
    logger.info("Root Route")
    return {"detail": "root"}

@app.get('/log/info')
async def info():
    logger.info("Info Route")
    return {"detail": "info"}

@app.get('/log/warning')
async def warning():
    logger.warning("Warning Route")
    return {"detail": "warning"}

@app.get('/log/error')
async def error():
    x = 1 / 0
    return {"detail": "error"}

@app.post('/model')
async def prediction(price: PriceRequest):

    if price.model_type == 'TABLE_LOOKUP':
        return {
            "model_type": "TABLE_LOOKUP",
            "model_version": "TL100",
            "price": 999999
        }
    elif price.model_type == 'ML_MODEL':
        return {
            "model_type": "ML_MODEL",
            "model_version": "ML100",
            "price": 444444
        }

    raise HTTPException(status_code=404, detail="Model Type/ Model Version not found")

