import redis
import os
from dotenv import load_dotenv

load_dotenv(".env")

r = redis.Redis(
    host= os.environ.get("CACHE_REDIS_HOST"),
    port= os.environ.get("CACHE_REDIS_PORT"),
    password= os.environ.get("CACHE_REDIS_PASSWORD"),
    username= "default",
    decode_responses= True,
    health_check_interval=5
)

r_url = redis.from_url("redis://default:hndMjjoMcnK4PONLa5bkn1anKmgKNAAE@viaduct.proxy.rlwy.net:51557")
"""this is an alternative way to establish a connection with redis server, localhost or what not"""


r_url.set("name", "freeman")


if __name__ == "__main__":
    print(r.get("name"))
