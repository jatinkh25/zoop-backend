from pydantic import BaseModel
from typing import Optional

class MenuItemBase(BaseModel):
    restaurant_id: int
    name: str
    description: Optional[str] = None
    price: float
    is_available: Optional[bool] = True
    image_url: Optional[str] = None

class MenuItemCreate(MenuItemBase):
    pass

class MenuItemUpdate(BaseModel):
    restaurant_id: Optional[int] = None
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    is_available: Optional[bool] = None
    image_url: Optional[str] = None
    
class MenuItem(MenuItemBase):
    id: int

    class Config:
        from_attributes = True