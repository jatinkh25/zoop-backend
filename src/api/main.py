from fastapi import APIRouter, Depends
from src.api.routes import (
    users,
    restaurants,
    menu_items,
    orders,
    order_items,
    reviews,
    payments
)
from src.dependencies import verify_supabase_token

api_router = APIRouter()

api_router.include_router(users.router, prefix="/users", tags=["users"], dependencies=[Depends(verify_supabase_token)])
api_router.include_router(restaurants.router, prefix="/restaurants", tags=["restaurants"], dependencies=[Depends(verify_supabase_token)])
api_router.include_router(menu_items.router, prefix="/menu-items", tags=["menu_items"], dependencies=[Depends(verify_supabase_token)])
api_router.include_router(orders.router, prefix="/orders", tags=["orders"], dependencies=[Depends(verify_supabase_token)])
api_router.include_router(order_items.router, prefix="/order-items", tags=["order_items"], dependencies=[Depends(verify_supabase_token)])
api_router.include_router(reviews.router, prefix="/reviews", tags=["reviews"], dependencies=[Depends(verify_supabase_token)])
api_router.include_router(payments.router, prefix="/payments", tags=["payments"], dependencies=[Depends(verify_supabase_token)])