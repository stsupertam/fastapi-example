from datetime import datetime
from typing import Union

from pydantic import BaseModel


class PriceResult(BaseModel):
    pos_dt: datetime
    request_id: str
    model_type: str
    model_version: str
    prediction_price: float
    confident_score: float

    class Config:
        orm_mode = True