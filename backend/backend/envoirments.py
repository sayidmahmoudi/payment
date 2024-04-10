from os import getenv

from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = getenv(
    "SECRET_KEY", "django-insecure-5-7a^hr%)p++4#=%1e%+p_epj06ngub@n71ogkm8-0y1!rf4al"
)


REDIS_HOST = getenv("REDIS_HOST", "accounting_redis")
REDIS_PORT = getenv("REDIS_PORT", 6379)

POSTGRES_USER = getenv("POSTGRES_USER", "root")
POSTGRES_PASSWORD = getenv("POSTGRES_PASSWORD", "root")
POSTGRES_DB = getenv("POSTGRES_DB", "wallet_postgres")
POSTGRES_NAME = getenv("POSTGRES_NAME", "postgres")
POSTGRES_HOST = getenv("POSTGRES_HOST", "localhost")
POSTGRES_PORT = getenv("POSTGRES_PORT", "5432")