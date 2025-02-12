from sqlalchemy.orm import Session
from fastapi import HTTPException
from src.models.menu_item import MenuItem
from src.schemas.menu_item import MenuItemCreate, MenuItemUpdate

class MenuItemService:
    @staticmethod
    def get_menu_items(db: Session, page_no: int = 0, limit: int = 100):
        offset = page_no * limit
        return db.query(MenuItem).offset(offset).limit(limit).all()

    @staticmethod
    def get_menu_item(db: Session, menu_item_id: int):
        menu_item = db.query(MenuItem).filter(MenuItem.id == menu_item_id).first()
        if not menu_item:
            raise HTTPException(status_code=404, detail="Menu item not found")
        return menu_item

    @staticmethod
    def create_menu_item(db: Session, menu_item: MenuItemCreate):
        db_menu_item = MenuItem(**menu_item.model_dump())
        db.add(db_menu_item)
        db.commit()
        db.refresh(db_menu_item)
        return db_menu_item

    @staticmethod
    def update_menu_item(db: Session, menu_item_id: int, menu_item: MenuItemUpdate):
        db_menu_item = MenuItemService.get_menu_item(db, menu_item_id)
        update_data = menu_item.model_dump(exclude_unset=True)
        for field, value in update_data.items():
            setattr(db_menu_item, field, value)
        db.commit()
        db.refresh(db_menu_item)
        return db_menu_item

    @staticmethod
    def delete_menu_item(db: Session, menu_item_id: int):
        db_menu_item = MenuItemService.get_menu_item(db, menu_item_id)
        db.delete(db_menu_item)
        db.commit()
        return db_menu_item