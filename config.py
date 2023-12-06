import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


class Config:
    CACHE_TYPE = "RedisCache"
    CACHE_REDIS_HOST = os.environ['CACHE_REDIS_HOST']
    CACHE_REDIS_PORT = os.environ['CACHE_REDIS_PORT']
    CACHE_REDIS_URL = os.environ['CACHE_REDIS_URL'] or "redis://"
    CACHE_REDIS_PASSWORD = os.environ['CACHE_REDIS_PASSWORD']
