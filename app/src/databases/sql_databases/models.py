from sqlalchemy import Boolean, Column, Float, Integer, String, DateTime
from sqlalchemy.orm import relationship

from src.databases.sql_databases.db_config import Base

class PriceResult(Base):
    __tablename__ = "prediction_result"

    pos_dt = Column(DateTime)
    request_id = Column(String, primary_key=True)
    model_type = Column(String)
    model_version = Column(String)
    prediction_price = Column(Float)
    confident_score = Column(Float)
