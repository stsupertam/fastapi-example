from datetime import datetime

from sqlalchemy.orm import Session

from src.databases.models.price_result import PriceResult as PriceResultModel
from src.schemas.price_result import PriceResult as PriceResultSchema


def create_price_result(db: Session, price_rslt: PriceResultSchema):
    db_price = PriceResultModel(
        pos_dt=price_rslt.pos_dt,
        request_id=price_rslt.request_id,
        model_type=price_rslt.model_type,
        model_version=price_rslt.model_version,
        prediction_price=price_rslt.prediction_price,
        confident_score=price_rslt.confident_score
    )
    db.add(db_price)
    db.commit()
    db.refresh(db_price)
    return db_price