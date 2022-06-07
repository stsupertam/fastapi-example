from datetime import datetime

from src.schemas.price_result import PriceResult as PriceResultSchema
from src.databases.nosql_databases.models import PriceResult as PriceResultModel

class PriceResultCRUD:

    @staticmethod
    async def create_price_result(price_rslt: PriceResultSchema):
        db_price = PriceResultModel(
            pos_dt=price_rslt.pos_dt,
            request_id=price_rslt.request_id,
            model_type=price_rslt.model_type,
            model_version=price_rslt.model_version,
            prediction_price=price_rslt.prediction_price,
            confident_score=price_rslt.confident_score
        )
        await db_price.create()
        return db_price

    @staticmethod
    async def get_price_result_by_id(request_id: str):
        return await PriceResultModel.find_one(PriceResultModel.request_id == request_id)
