from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from enum import Enum

class OrderStatus(str, Enum):
    pending = "pending"
    preparing = "preparing"
    on_the_way = "on the way"
    delivered = "delivered"
    cancelled = "cancelled"

class OrderBase(BaseModel):
    customer_id: Optional[int] = None
    restaurant_id: Optional[int] = None
    delivery_person_id: Optional[int] = None
    order_status: OrderStatus
    total_price: float

class OrderCreate(OrderBase):
    pass

class OrderUpdate(BaseModel):
    customer_id: Optional[int] = None
    restaurant_id: Optional[int] = None
    delivery_person_id: Optional[int] = None
    order_status: Optional[OrderStatus] = None
    total_price: Optional[float] = None

class Order(OrderBase):
    id: int
    order_date: datetime

    class Config:
        from_attributes = True