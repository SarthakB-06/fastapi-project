import joblib
import pandas as pd
from app.core.config import settings
from app.cache.redis_cache import get_cached_data , set_cached_data


model = joblib.load(settings.MODEL_FILE_PATH)


def make_prediction(data:dict):
    cache_key = " ".join([str(val) for val in data.values()])
    cached = get_cached_data(cache_key)
    if cached:
        return cached
    df = pd.DataFrame([data])
    prediction = model.predict(df)[0]
    result = {"predicted_price" : round(prediction , 2)}
    set_cached_data(cache_key , prediction)
    return result



