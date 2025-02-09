import sentry_sdk
from fastapi import FastAPI
from fastapi.routing import APIRoute
from starlette.middleware.cors import CORSMiddleware

from src.api.main import api_router
from src.core.config import settings
from src.db.base import Base, engine

def custom_generate_unique_id(route: APIRoute) -> str:
    # Return a custom unique id combining the first tag and the route name.
    # Fallback to route.name if no tags are provided.
    return f"{route.tags[0]}-{route.name}" if route.tags else route.name

# Initialize Sentry if a DSN is provided and the environment is not "local"
if settings.SENTRY_DSN and settings.ENVIRONMENT != "local":
    sentry_sdk.init(dsn=str(settings.SENTRY_DSN), enable_tracing=True)

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    generate_unique_id_function=custom_generate_unique_id,
)

# Apply CORS middleware if origins are specified
if settings.all_cors_origins:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.all_cors_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

# Optionally create database tables on startup
Base.metadata.create_all(bind=engine)

# Include our central API router at the configured prefix
app.include_router(api_router, prefix=settings.API_V1_STR)

@app.get("/")
def read_root():
    return {"Hello": "World"}


