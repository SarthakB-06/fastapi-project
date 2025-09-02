from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator
from app.api import routes_auth, routes_predict
from app.middlewares.logging_middleware import LoggingMiddleware
from app.core.exceptions import register_exception_handlers


app = FastAPI(title="Car Price Prediction API")
app.add_middleware(LoggingMiddleware)


# link endpoints
app.include_router(routes_auth.router , tags=['Auth'])
app.include_router(routes_predict.router , tags=['Predict'])


# monitoring using prometheus
Instrumentator().instrument(app).expose(app)
# add exception handlers
register_exception_handlers(app)