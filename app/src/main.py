import random
import uuid
from datetime import datetime

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from starlette.middleware.cors import CORSMiddleware

from src.common_libs.middleware import LoggingMiddleware
from src.common_libs.constants.settings import app_settings
from src.common_libs.utils.logging import logger
from src.schemas.price_request import PriceRequest
from src.schemas.price_result import PriceResult
from src.databases.operator.db_price_result import create_price_result
from src.databases.db_config import Base, engine, get_db


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
async def prediction(price: PriceRequest, db: Session = Depends(get_db)):
    request_id = str(uuid.uuid1())
    prediction_price = round(random.uniform(100000, 1000000), 2)
    confident_score = round(random.uniform(0, 100), 2)

    if price.model_type == 'TABLE_LOOKUP':
        result = {
            "pos_dt": datetime.now(),
            "request_id": request_id,
            "model_type": "TABLE_LOOKUP",
            "model_version": "T100",
            "prediction_price": prediction_price,
            "confident_score": confident_score
        }
    elif price.model_type == 'ML_MODEL':
        result = {
            "pos_dt": datetime.now(),
            "request_id": request_id,
            "model_type": "ML_MODEL",
            "model_version": "M100",
            "prediction_price": prediction_price,
            "confident_score": confident_score
        }
    else:
        raise HTTPException(status_code=404, detail="Model Type/ Model Version not found")

    model = PriceResult.parse_obj(result)

    return create_price_result(db, model)

