import random
import uuid
from typing import Any

from datetime import datetime

from fastapi import APIRouter
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from src.schemas.price_request import PriceRequest
from src.schemas.price_result import PriceResult
from src.databases.nosql_databases.crud.price_result import PriceResultCRUD
# from src.databases.nosql_databases.db_config import get_db

#APIRouter creates path operations for user module
router = APIRouter(
    prefix="/nosql",
    responses={404: {"description": "Not found"}},
)

# @router.get('/result/{pred_req_id}')
# async def prediction(pred_req_id: str, db: Any = Depends(get_db)):
#     return PriceResultCRUD.get_price_result_by_id(db, pred_req_id)

@router.post('/prediction')
async def prediction(price: PriceRequest):
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

    result = await PriceResultCRUD.create_price_result(model) 
    
    return result
