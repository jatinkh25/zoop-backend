from sqlalchemy import Column, BigInteger, Text
from src.db.base import Base

class Restaurant(Base):
    __tablename__ = "restaurants"

    id = Column(BigInteger, primary_key=True, index=True)
    name = Column(Text, nullable=False)
    address = Column(Text, nullable=False)
    phone_number = Column(Text, unique=True, nullable=False)
    email = Column(Text, unique=True, nullable=False)
    opening_hours = Column(Text)

