import os
from dotenv import load_dotenv

load_dotenv(".env")


class config(object):
    CACHE_TYPE = "RedisCache"
    CACHE_REDIS_HOST = os.environ['CACHE_REDIS_HOST']
    CACHE_REDIS_PORT = os.environ['CACHE_REDIS_PORT']
    CACHE_REDIS_URL = os.environ['CACHE_REDIS_URL']
    CACHE_REDIS_PASSWORD = os.environ['CACHE_REDIS_PASSWORD']
