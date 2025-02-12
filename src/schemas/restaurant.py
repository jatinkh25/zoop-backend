from pydantic import BaseModel
from typing import Optional, List
from src.schemas.menu_item import MenuItem  # Assuming you have a MenuItem schema

class RestaurantBase(BaseModel):
    name: str
    opening_hours: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None

class RestaurantCreate(RestaurantBase):
    pass

class RestaurantUpdate(BaseModel):
    name: Optional[str] = None
    opening_hours: Optional[str] = None
    discount: Optional[float] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None

    # If you want to update the top_menu_items, you might accept an array of menu item IDs here
    top_menu_item_ids: Optional[List[int]] = None

class Restaurant(RestaurantBase):
    id: int
    # Include the related menu items
    top_menu_items: List[MenuItem] = []

    class Config:
        from_attributes = True