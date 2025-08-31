import json
import redis
from app.core.config import settings

redis_client = redis.Redis.from_url(settings.REDIS_URL)


def get_cached_data(key : str):
    value = redis_client.get(key)
    if value:
        return json.loads(value)
    return None

def set_cached_data(key : str, value:dict ,  ex : int = 300):
    redis_client.setex(key , ex , json.dumps(value))

