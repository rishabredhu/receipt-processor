from pydantic import BaseModel, Field, field_validator
from typing import List
from datetime import date, time
import re

class Item(BaseModel):
    shortDescription: str = Field(..., example="Mountain Dew 12PK")
    price: str = Field(..., example="6.49")

    @field_validator('shortDescription')
    def validate_short_description(cls, value):
        if not re.match(r"^[\w\s\-]+$", value):
            raise ValueError('Invalid short description')
        return value

    @field_validator('price')
    def validate_price(cls, value):
        if not re.match(r"^\d+\.\d{2}$", value):
            raise ValueError('Invalid price format')
        return value

class Receipt(BaseModel):
    retailer: str = Field(..., example="M&M Corner Market")
    purchaseDate: date = Field(..., example="2022-01-01")
    purchaseTime: time = Field(..., example="13:01")
    items: List[Item] = Field(..., min_items=1)
    total: str = Field(..., example="6.49")

class ReceiptResponse(BaseModel):
    id: str

class PointsResponse(BaseModel):
    points: int