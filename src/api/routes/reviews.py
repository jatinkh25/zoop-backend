from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from src.schemas import Review, ReviewCreate, ReviewUpdate
from src.services import ReviewService
from src.db.base import get_db

router = APIRouter()

@router.get("/", response_model=List[Review])
def get_reviews(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return ReviewService.get_reviews(db, skip, limit)

@router.post("/", response_model=Review)
def create_review(review: ReviewCreate, db: Session = Depends(get_db)):
    return ReviewService.create_review(db, review)

@router.get("/{review_id}", response_model=Review)
def get_review(review_id: int, db: Session = Depends(get_db)):
    return ReviewService.get_review(db, review_id)

@router.put("/{review_id}", response_model=Review)
def update_review(review_id: int, review: ReviewUpdate, db: Session = Depends(get_db)):
    return ReviewService.update_review(db, review_id, review)

@router.delete("/{review_id}", response_model=Review)
def delete_review(review_id: int, db: Session = Depends(get_db)):
    return ReviewService.delete_review(db, review_id)