from fastapi import FastAPI

from app.api.routes.health import router as health_router
from app.api.routes.linkedin import router as linkedin_router

app = FastAPI(title="Veera Backend")


app.include_router(health_router)
app.include_router(linkedin_router, prefix="/linkedin")


@app.get("/")
def root():
    return {
        "message": "Veera Backend Running"
    }