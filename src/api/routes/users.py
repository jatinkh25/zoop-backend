from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from src.schemas import User, UserCreate, UserUpdate
from src.services import UserService
from src.db.base import get_db

router = APIRouter()

@router.get("", response_model=List[User])
def get_users(page_no: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return UserService.get_users(db, page_no, limit)

@router.post("", response_model=User)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return UserService.create_user(db, user)

@router.get("/{user_id}", response_model=User)
def get_user(user_id: int, db: Session = Depends(get_db)):
    return UserService.get_user(db, user_id)

@router.put("/{user_id}", response_model=User)
def update_user(user_id: int, user: UserUpdate, db: Session = Depends(get_db)):
    return UserService.update_user(db, user_id, user)

@router.delete("/{user_id}", response_model=User)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    return UserService.delete_user(db, user_id)