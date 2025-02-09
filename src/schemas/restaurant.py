from pydantic import BaseModel
from typing import Optional

class RestaurantBase(BaseModel):
    name: str
    address: str
    phone_number: str
    email: str
    opening_hours: Optional[str] = None

class RestaurantCreate(RestaurantBase):
    pass

class RestaurantUpdate(BaseModel):
    name: Optional[str] = None
    address: Optional[str] = None
    phone_number: Optional[str] = None
    email: Optional[str] = None
    opening_hours: Optional[str] = None

class Restaurant(RestaurantBase):
    id: int

    class Config:
        from_attributes = True