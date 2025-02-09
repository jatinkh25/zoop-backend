from .users import router as users_router
from .restaurants import router as restaurants_router
from .menu_items import router as menu_items_router
from .orders import router as orders_router
from .order_items import router as order_items_router
from .reviews import router as reviews_router
from .payments import router as payments_router

__all__ = ["users_router", "restaurants_router", "menu_items_router", "orders_router", "order_items_router", "reviews_router", "payments_router"]