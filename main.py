from redis import Redis
import os
from dotenv import load_dotenv

load_dotenv(".env")

r = Redis(
    host= os.environ.get("CACHE_REDIS_HOST"),
    port= os.environ.get("CACHE_REDIS_PORT"),
    password= os.environ.get("CACHE_REDIS_PASSWORD"),
    username= "default",
    decode_responses= True,
    health_check_interval=5
)


r.set("name", "freeman")


if __name__ == "__main__":
    print(r.get("name"))
