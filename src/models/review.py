from sqlalchemy import Column, BigInteger, Integer, Text, DateTime, ForeignKey, CheckConstraint
from sqlalchemy.sql import func
from src.db.base import Base

class Review(Base):
    __tablename__ = "reviews"

    id = Column(BigInteger, primary_key=True, index=True)
    customer_id = Column(BigInteger, ForeignKey("users.id", ondelete="SET NULL"))
    restaurant_id = Column(BigInteger, ForeignKey("restaurants.id", ondelete="CASCADE"))
    rating = Column(Integer, nullable=False)
    comment = Column(Text)
    review_date = Column(DateTime(timezone=True), server_default=func.now())
    
    __table_args__ = (
        CheckConstraint("rating >= 1 and rating <= 5", name="rating_check"),
    )

