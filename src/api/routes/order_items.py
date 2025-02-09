from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from src.schemas import OrderItem, OrderItemCreate, OrderItemUpdate
from src.services import OrderItemService
from src.db.base import get_db

router = APIRouter()

@router.get("/", response_model=List[OrderItem])
def get_order_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return OrderItemService.get_order_items(db, skip, limit)

@router.post("/", response_model=OrderItem)
def create_order_item(order_item: OrderItemCreate, db: Session = Depends(get_db)):
    return OrderItemService.create_order_item(db, order_item)

@router.get("/{order_item_id}", response_model=OrderItem)
def get_order_item(order_item_id: int, db: Session = Depends(get_db)):
    return OrderItemService.get_order_item(db, order_item_id)

@router.put("/{order_item_id}", response_model=OrderItem)
def update_order_item(order_item_id: int, order_item: OrderItemUpdate, db: Session = Depends(get_db)):
    return OrderItemService.update_order_item(db, order_item_id, order_item)

@router.delete("/{order_item_id}", response_model=OrderItem)
def delete_order_item(order_item_id: int, db: Session = Depends(get_db)):
    return OrderItemService.delete_order_item(db, order_item_id)