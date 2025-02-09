from sqlalchemy import Column, BigInteger, Text, Numeric, Boolean, ForeignKey
from src.db.base import Base

class MenuItem(Base):
    __tablename__ = "menu_items"

    id = Column(BigInteger, primary_key=True, index=True)
    restaurant_id = Column(BigInteger, ForeignKey("restaurants.id", ondelete="CASCADE"), nullable=False)
    name = Column(Text, nullable=False)
    description = Column(Text)
    price = Column(Numeric(10, 2), nullable=False)
    is_available = Column(Boolean, default=True)

