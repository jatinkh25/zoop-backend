from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from src.schemas import Order, OrderCreate, OrderUpdate
from src.services import OrderService
from src.db.base import get_db

router = APIRouter()

@router.get("/", response_model=List[Order])
def get_orders(page_no: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return OrderService.get_orders(db, page_no, limit)

@router.post("/", response_model=Order)
def create_order(order: OrderCreate, db: Session = Depends(get_db)):
    return OrderService.create_order(db, order)

@router.get("/{order_id}", response_model=Order)
def get_order(order_id: int, db: Session = Depends(get_db)):
    return OrderService.get_order(db, order_id)

@router.put("/{order_id}", response_model=Order)
def update_order(order_id: int, order: OrderUpdate, db: Session = Depends(get_db)):
    return OrderService.update_order(db, order_id, order)

@router.delete("/{order_id}", response_model=Order)
def delete_order(order_id: int, db: Session = Depends(get_db)):
    return OrderService.delete_order(db, order_id)