from sqlalchemy.orm import Session, joinedload
from fastapi import HTTPException
from src.models.restaurant import Restaurant
from src.schemas.restaurant import RestaurantCreate, RestaurantUpdate

class RestaurantService:
    @staticmethod
    def get_restaurants(db: Session, page_no: int = 0, limit: int = 100):
        offset = page_no * limit
        return db.query(Restaurant)\
                 .options(joinedload(Restaurant.top_menu_items))\
                 .offset(offset)\
                 .limit(limit)\
                 .all()

    @staticmethod
    def get_restaurant(db: Session, restaurant_id: int):
        restaurant = db.query(Restaurant)\
                       .options(joinedload(Restaurant.top_menu_items))\
                       .filter(Restaurant.id == restaurant_id)\
                       .first()
        if not restaurant:
            raise HTTPException(status_code=404, detail="Restaurant not found")
        return restaurant

    @staticmethod
    def create_restaurant(db: Session, restaurant: RestaurantCreate):
        db_restaurant = Restaurant(**restaurant.model_dump())
        db.add(db_restaurant)
        db.commit()
        db.refresh(db_restaurant)
        return db_restaurant

    @staticmethod
    def update_restaurant(db: Session, restaurant_id: int, restaurant: RestaurantUpdate):
        db_restaurant = RestaurantService.get_restaurant(db, restaurant_id)
        update_data = restaurant.model_dump(exclude_unset=True)
        for field, value in update_data.items():
            setattr(db_restaurant, field, value)
        db.commit()
        db.refresh(db_restaurant)
        return db_restaurant

    @staticmethod
    def delete_restaurant(db: Session, restaurant_id: int):
        db_restaurant = RestaurantService.get_restaurant(db, restaurant_id)
        db.delete(db_restaurant)
        db.commit()
        return db_restaurant