from sqlalchemy.orm import Session
from fastapi import HTTPException
from src.models.user import User
from src.schemas.user import UserCreate, UserUpdate

class UserService:
    @staticmethod
    def get_users(db: Session, page_no: int = 0, limit: int = 100):
        offset = page_no * limit
        return db.query(User).offset(offset).limit(limit).all()

    @staticmethod
    def get_user(db: Session, user_id: int):
        user = db.query(User).filter(User.id == user_id).first()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return user

    @staticmethod
    def create_user(db: Session, user: UserCreate):
        db_user = User(**user.model_dump())
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user

    @staticmethod
    def update_user(db: Session, user_id: int, user: UserUpdate):
        db_user = UserService.get_user(db, user_id)
        update_data = user.model_dump(exclude_unset=True)
        for field, value in update_data.items():
            setattr(db_user, field, value)
        db.commit()
        db.refresh(db_user)
        return db_user

    @staticmethod
    def delete_user(db: Session, user_id: int):
        db_user = UserService.get_user(db, user_id)
        db.delete(db_user)
        db.commit()
        return db_user