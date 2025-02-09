from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class ReviewBase(BaseModel):
    customer_id: Optional[int] = None
    restaurant_id: int
    rating: int
    comment: Optional[str] = None

class ReviewCreate(ReviewBase):
    pass

class ReviewUpdate(BaseModel):
    customer_id: Optional[int] = None
    restaurant_id: Optional[int] = None
    rating: Optional[int] = None
    comment: Optional[str] = None

class Review(ReviewBase):
    id: int
    review_date: datetime

    class Config:
        from_attributes = True