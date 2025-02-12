from sqlalchemy.orm import Session
from fastapi import HTTPException
from src.models.order import Order
from src.schemas.order import OrderCreate, OrderUpdate

class OrderService:
    @staticmethod
    def get_orders(db: Session, page_no: int = 0, limit: int = 100):
        offset = page_no * limit
        return db.query(Order).offset(offset).limit(limit).all()

    @staticmethod
    def get_order(db: Session, order_id: int):
        order = db.query(Order).filter(Order.id == order_id).first()
        if not order:
            raise HTTPException(status_code=404, detail="Order not found")
        return order

    @staticmethod
    def create_order(db: Session, order: OrderCreate):
        db_order = Order(**order.model_dump())
        db.add(db_order)
        db.commit()
        db.refresh(db_order)
        return db_order

    @staticmethod
    def update_order(db: Session, order_id: int, order: OrderUpdate):
        db_order = OrderService.get_order(db, order_id)
        update_data = order.model_dump(exclude_unset=True)
        for field, value in update_data.items():
            setattr(db_order, field, value)
        db.commit()
        db.refresh(db_order)
        return db_order

    @staticmethod
    def delete_order(db: Session, order_id: int):
        db_order = OrderService.get_order(db, order_id)
        db.delete(db_order)
        db.commit()
        return db_order