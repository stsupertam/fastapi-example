from typing import Union

from pydantic import BaseModel


class PriceRequest(BaseModel):
    model_type: str
    model_version: str
    model: str
    year: int
