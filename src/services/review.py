from sqlalchemy.orm import Session
from fastapi import HTTPException
from src.models.review import Review
from src.schemas.review import ReviewCreate, ReviewUpdate

class ReviewService:
    @staticmethod
    def get_reviews(db: Session, page_no: int = 0, limit: int = 100):
        offset = page_no * limit
        return db.query(Review).offset(offset).limit(limit).all()

    @staticmethod
    def get_review(db: Session, review_id: int):
        review = db.query(Review).filter(Review.id == review_id).first()
        if not review:
            raise HTTPException(status_code=404, detail="Review not found")
        return review

    @staticmethod
    def create_review(db: Session, review: ReviewCreate):
        db_review = Review(**review.model_dump())
        db.add(db_review)
        db.commit()
        db.refresh(db_review)
        return db_review

    @staticmethod
    def update_review(db: Session, review_id: int, review: ReviewUpdate):
        db_review = ReviewService.get_review(db, review_id)
        update_data = review.model_dump(exclude_unset=True)
        for field, value in update_data.items():
            setattr(db_review, field, value)
        db.commit()
        db.refresh(db_review)
        return db_review

    @staticmethod
    def delete_review(db: Session, review_id: int):
        db_review = ReviewService.get_review(db, review_id)
        db.delete(db_review)
        db.commit()
        return db_review