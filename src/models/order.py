from sqlalchemy import Column, BigInteger, Text, Numeric, DateTime, ForeignKey, CheckConstraint
from sqlalchemy.sql import func
from src.db.base import Base

class Order(Base):
    __tablename__ = "orders"

    id = Column(BigInteger, primary_key=True, index=True)
    customer_id = Column(BigInteger, ForeignKey("users.id", ondelete="SET NULL"))
    restaurant_id = Column(BigInteger, ForeignKey("restaurants.id", ondelete="SET NULL"))
    delivery_person_id = Column(BigInteger, ForeignKey("users.id", ondelete="SET NULL"))
    order_status = Column(Text, nullable=False)
    total_price = Column(Numeric(10, 2), nullable=False)
    order_date = Column(DateTime(timezone=True), server_default=func.now())
    
    __table_args__ = (
        CheckConstraint("order_status in ('pending','preparing','on the way','delivered','cancelled')", name="order_status_check"),
    )

