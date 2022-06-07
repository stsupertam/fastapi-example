from datetime import datetime

from sqlalchemy.orm import Session

from src.schemas.price_result import PriceResult as PriceResultSchema
from src.databases.sql_databases.models import PriceResult as PriceResultModel

class PriceResultCRUD:

    @staticmethod
    def create_price_result(db: Session, price_rslt: PriceResultSchema):
        db.add(db_price)
        db.commit()
        db.refresh(db_price)
        return db_price

    @staticmethod
    def get_price_result_by_id(db: Session, request_id: str):
        return db.query(PriceResultModel).filter(PriceResultModel.request_id == request_id).first()