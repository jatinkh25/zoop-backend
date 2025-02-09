from fastapi import APIRouter
from src.api.routes import (
    users,
    restaurants,
    menu_items,
    orders,
    order_items,
    reviews,
    payments
)

api_router = APIRouter()

api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(restaurants.router, prefix="/restaurants", tags=["restaurants"])
api_router.include_router(menu_items.router, prefix="/menu-items", tags=["menu_items"])
api_router.include_router(orders.router, prefix="/orders", tags=["orders"])
api_router.include_router(order_items.router, prefix="/order-items", tags=["order_items"])
api_router.include_router(reviews.router, prefix="/reviews", tags=["reviews"])
api_router.include_router(payments.router, prefix="/payments", tags=["payments"])