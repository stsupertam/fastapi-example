from bson import ObjectId
from datetime import datetime

from beanie import Document
from pydantic import BaseModel, Field

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

# class PyObjectId(ObjectId):
#     @classmethod
#     def __get_validators__(cls):
#         yield cls.validate

#     @classmethod
#     def validate(cls, v):
#         if not ObjectId.is_valid(v):
#             raise ValueError("Invalid objectid")
#         return ObjectId(v)

#     @classmethod
#     def __modify_schema__(cls, field_schema):
#         field_schema.update(type="string")


# class PriceResult(BaseModel):
#     id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
#     pos_dt: datetime = Field(...)
#     request_id: str = Field(...)
#     model_type: str = Field(...)
#     model_version: str = Field(...)
#     prediction_price: float = Field(...)
#     confident_score: float = Field(...)

#     class Config:
#         json_encoders = {ObjectId: str}
#         schema_extra = {
#             "example": {
#                 "request_id": "ID99998888",
#                 "model_type": "ML_MODEL",
#                 "model_version": "M100",
#                 "prediction_price": 999999.99,
#                 "confident_score": 999999.99,
#             }
#         }