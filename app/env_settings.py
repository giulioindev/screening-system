from pydantic import Field, computed_field
from pydantic_settings import BaseSettings, SettingsConfigDict


class EnvSettings(BaseSettings):
    """App environment variables."""

    secret_key: str = Field(description="Django secret key.")
    postgres_db: str = Field(description="Database name")
    postgres_user: str = Field(description="Database user name")
    postgres_password: str = Field(description="Database password")
    postgres_host: str = Field(description="Database host")
    postgres_port: int = Field(description="Database port")
    redis_host: str = Field(description="Redis host")
    redis_port: int = Field(description="Redis port")

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    @computed_field
    @property
    def redis_url(self) -> str:
        """Redis URL.

        Returns:
            str: Redis URL.
        """
        return f"redis://{self.redis_host}:{self.redis_port}"
