from bson import ObjectId
from datetime import datetime

from beanie import Document

from src.databases.sql_databases.db_config import Base

class PriceResult(Document):
    pos_dt: datetime
    request_id: str
    model_type: str
    model_version: str
    prediction_price: float
    confident_score: float

    class Settings:
        name = "prediction_result"
    
    class Config:
        schema_extra = {
            "example": {
                "request_id": "ID99998888",
                "model_type": "ML_MODEL",
                "model_version": "M100",
                "prediction_price": 999999.99,
                "confident_score": 999999.99,
            }
        }
