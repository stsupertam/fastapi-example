from typing import Union

from pydantic import BaseModel


class PriceRequest(BaseModel):
    request_id: str
    model_type: str
    model_version: str
    model: str
    year: int
