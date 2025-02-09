from pydantic import BaseModel
from typing import Optional
from enum import Enum

class UserType(str, Enum):
    customer = "customer"
    delivery_person = "delivery_person"

class UserBase(BaseModel):
    name: str
    email: str
    phone_number: str
    address: Optional[str] = None
    user_type: UserType

class UserCreate(UserBase):
    password: str

class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    phone_number: Optional[str] = None
    address: Optional[str] = None
    user_type: Optional[UserType] = None
    password: Optional[str] = None

class User(UserBase):
    id: int

    class Config:
        from_attributes = True

