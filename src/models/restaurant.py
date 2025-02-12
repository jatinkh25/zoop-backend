from sqlalchemy import Column, BigInteger, Text, Float, Table, ForeignKey
from sqlalchemy.orm import relationship
from src.db.base import Base

# Association table for top menu items
restaurant_top_menu_items = Table(
    'restaurant_top_menu_items',
    Base.metadata,
    Column('restaurant_id', BigInteger, ForeignKey('restaurants.id', ondelete='CASCADE'), primary_key=True),
    Column('menu_item_id', BigInteger, ForeignKey('menu_items.id', ondelete='CASCADE'), primary_key=True)
)

class Restaurant(Base):
    __tablename__ = "restaurants"

    id = Column(BigInteger, primary_key=True, index=True)
    name = Column(Text, nullable=False)
    opening_hours = Column(Text)
    discount = Column(Float, nullable=True)
    
    # Location fields
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    
    # Define a many-to-many relationship to MenuItem
    top_menu_items = relationship(
        "MenuItem",
        secondary=restaurant_top_menu_items,
        lazy="joined"  # Eager loading: SQLAlchemy will automatically join this table when querying Restaurant
    )

