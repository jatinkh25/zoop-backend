from sqlalchemy import Column, BigInteger, Text, CheckConstraint
from src.db.base import Base

class User(Base):
    __tablename__ = "users"

    id = Column(BigInteger, primary_key=True, index=True)
    name = Column(Text, nullable=False)
    email = Column(Text, unique=True, nullable=False)
    password = Column(Text, nullable=False)
    phone_number = Column(Text, unique=True, nullable=False)
    address = Column(Text)
    user_type = Column(Text, nullable=False)
    
    __table_args__ = (
        CheckConstraint("user_type in ('customer','delivery_person')", name="user_type_check"),
    )