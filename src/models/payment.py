from sqlalchemy import Column, BigInteger, Text, DateTime, ForeignKey, CheckConstraint
from sqlalchemy.sql import func
from src.db.base import Base

class Payment(Base):
    __tablename__ = "payments"

    id = Column(BigInteger, primary_key=True, index=True)
    order_id = Column(BigInteger, ForeignKey("orders.id", ondelete="CASCADE"), nullable=False)
    payment_method = Column(Text, nullable=False)
    payment_status = Column(Text, nullable=False)
    payment_date = Column(DateTime(timezone=True), server_default=func.now())
    
    __table_args__ = (
        CheckConstraint("payment_method in ('credit_card','debit_card','paypal','cash')", name="payment_method_check"),
        CheckConstraint("payment_status in ('pending','completed','failed')", name="payment_status_check"),
    )