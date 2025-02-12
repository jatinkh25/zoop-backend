from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from src.schemas import MenuItem, MenuItemCreate, MenuItemUpdate
from src.services import MenuItemService
from src.db.base import get_db

router = APIRouter()

@router.get("", response_model=List[MenuItem])
def get_menu_items(page_no: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return MenuItemService.get_menu_items(db, page_no, limit)

@router.post("", response_model=MenuItem)
def create_menu_item(menu_item: MenuItemCreate, db: Session = Depends(get_db)):
    return MenuItemService.create_menu_item(db, menu_item)

@router.get("/{menu_item_id}", response_model=MenuItem)
def get_menu_item(menu_item_id: int, db: Session = Depends(get_db)):
    return MenuItemService.get_menu_item(db, menu_item_id)

@router.put("/{menu_item_id}", response_model=MenuItem)
def update_menu_item(menu_item_id: int, menu_item: MenuItemUpdate, db: Session = Depends(get_db)):
    return MenuItemService.update_menu_item(db, menu_item_id, menu_item)

@router.delete("/{menu_item_id}", response_model=MenuItem)
def delete_menu_item(menu_item_id: int, db: Session = Depends(get_db)):
    return MenuItemService.delete_menu_item(db, menu_item_id)