from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from src.schemas import Restaurant, RestaurantCreate, RestaurantUpdate
from src.services import RestaurantService
from src.db.base import get_db

router = APIRouter()

@router.get("/", response_model=List[Restaurant])
def get_restaurants(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return RestaurantService.get_restaurants(db, skip, limit)

@router.post("/", response_model=Restaurant)
def create_restaurant(restaurant: RestaurantCreate, db: Session = Depends(get_db)):
    return RestaurantService.create_restaurant(db, restaurant)

@router.get("/{restaurant_id}", response_model=Restaurant)
def get_restaurant(restaurant_id: int, db: Session = Depends(get_db)):
    return RestaurantService.get_restaurant(db, restaurant_id)

@router.put("/{restaurant_id}", response_model=Restaurant)
def update_restaurant(restaurant_id: int, restaurant: RestaurantUpdate, db: Session = Depends(get_db)):
    return RestaurantService.update_restaurant(db, restaurant_id, restaurant)

@router.delete("/{restaurant_id}", response_model=Restaurant)
def delete_restaurant(restaurant_id: int, db: Session = Depends(get_db)):
    return RestaurantService.delete_restaurant(db, restaurant_id)