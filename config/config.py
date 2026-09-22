import os
from dotenv import load_dotenv

load_dotenv()


class BaseConfig:
    """Shared default settings."""
    SECRET_KEY: str = os.environ.get("SECRET_KEY", "default-secret-key")
    JSON_SORT_KEYS: bool = False

    # Feature flags / domain config
    SEED_DATA: bool = False
    DEFAULT_PAGE_SIZE: int = 20


class DevelopmentConfig(BaseConfig):
    """Local development."""
    DEBUG: bool = True
    ENV: str = "development"
    SEED_DATA: bool = True


class TestingConfig(BaseConfig):
    """Unit/integration tests."""
    TESTING: bool = True
    DEBUG: bool = True
    ENV: str = "testing"
    SEED_DATA: bool = True
    WTF_CSRF_ENABLED: bool = False


class ProductionConfig(BaseConfig):
    """Production."""
    DEBUG: bool = False
    ENV: str = "production"
    SEED_DATA: bool = False


config_by_name = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,
    "default": DevelopmentConfig,
}
