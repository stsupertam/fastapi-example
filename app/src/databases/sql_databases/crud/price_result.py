from datetime import datetime

from sqlalchemy.orm import Session

from src.schemas.price_result import PriceResult as PriceResultSchema
from src.databases.sql_databases.db_config import database
from src.databases.sql_databases.models import PriceResult as PriceResultModel

class PriceResultCRUD:

    @staticmethod
    async def create_price_result(price_rslt: PriceResultSchema):
        db_price = PriceResultModel()

        query = db_price.__table__.insert().values(**price_rslt.dict())

        await database.execute(query)
        
        return price_rslt

    @staticmethod
    async def get_price_result_by_id(request_id: str):
        db_price = PriceResultModel()

        query = db_price.__table__.select().where(PriceResultModel.request_id == request_id)
        
        result = await database.fetch_one(query)
        
        return result