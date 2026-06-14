from fastapi import FastAPI

from app.api.v1.health.router import router as health_router
from app.core.config import settings


app = FastAPI(
    title=settings.APP_NAME
)

app.include_router(
    health_router,
    prefix="/health",
    tags=["Health"]
)


@app.get("/")
def root():
    return {
        "application": settings.APP_NAME
    }