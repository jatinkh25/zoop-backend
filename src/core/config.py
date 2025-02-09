from typing import Annotated, Any, Literal
from pydantic import (
    AnyUrl,
    BeforeValidator,
    HttpUrl,
    PostgresDsn,
    computed_field,
)
from pydantic_core import MultiHostUrl
from pydantic_settings import BaseSettings


def parse_cors(v: Any) -> list[str] | str:
    """
    Parses a comma-separated string or a list into a list of strings.
    This is useful for the BACKEND_CORS_ORIGINS field when read from an env var.
    """
    if isinstance(v, str) and not v.startswith("["):
        return [i.strip() for i in v.split(",")]
    elif isinstance(v, list | str):
        return v
    raise ValueError(v)


class Settings(BaseSettings):
    API_V1_STR: str
    FRONTEND_HOST: str
    ENVIRONMENT: Literal["local", "staging", "production"]
    PROJECT_NAME: str
    SENTRY_DSN: HttpUrl | None = None
    POSTGRES_SERVER: str
    POSTGRES_PORT: int
    POSTGRES_USER: str
    # POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    BACKEND_CORS_ORIGINS: Annotated[
        list[AnyUrl] | str, BeforeValidator(parse_cors)
    ] = []

    @computed_field
    @property
    def SQLALCHEMY_DATABASE_URI(self) -> PostgresDsn:
        """
        Constructs the database URI from its individual components.
        """
        return str(MultiHostUrl.build(
            scheme="postgresql+psycopg",
            username=self.POSTGRES_USER,
            # password=self.POSTGRES_PASSWORD,
            host=self.POSTGRES_SERVER,
            port=self.POSTGRES_PORT,
            path=self.POSTGRES_DB,
        ))
    
    @computed_field
    @property
    def all_cors_origins(self) -> list[str]:
        """
        Combines backend CORS origins with the frontend host.
        """
        return [str(origin).rstrip("/") for origin in self.BACKEND_CORS_ORIGINS] + [
            self.FRONTEND_HOST
        ]
    
    class Config:
        env_file = ".env"
        env_file_encoding = 'utf-8'
        env_ignore_empty = True
        extra = "ignore"


settings = Settings()
print("settings", settings.SQLALCHEMY_DATABASE_URI)