from sqlalchemy.orm import Session
from fastapi import HTTPException
from src.models.order_item import OrderItem
from src.schemas.order_item import OrderItemCreate, OrderItemUpdate

class OrderItemService:
    @staticmethod
    def get_order_items(db: Session, skip: int = 0, limit: int = 100):
        return db.query(OrderItem).offset(skip).limit(limit).all()

    @staticmethod
    def get_order_item(db: Session, order_item_id: int):
        order_item = db.query(OrderItem).filter(OrderItem.id == order_item_id).first()
        if not order_item:
            raise HTTPException(status_code=404, detail="Order item not found")
        return order_item

    @staticmethod
    def create_order_item(db: Session, order_item: OrderItemCreate):
        db_order_item = OrderItem(**order_item.model_dump())
        db.add(db_order_item)
        db.commit()
        db.refresh(db_order_item)
        return db_order_item

    @staticmethod
    def update_order_item(db: Session, order_item_id: int, order_item: OrderItemUpdate):
        db_order_item = OrderItemService.get_order_item(db, order_item_id)
        update_data = order_item.model_dump(exclude_unset=True)
        for field, value in update_data.items():
            setattr(db_order_item, field, value)
        db.commit()
        db.refresh(db_order_item)
        return db_order_item

    @staticmethod
    def delete_order_item(db: Session, order_item_id: int):
        db_order_item = OrderItemService.get_order_item(db, order_item_id)
        db.delete(db_order_item)
        db.commit()
        return db_order_item