from fastapi import FastAPI
from app.api.routes.feed_ai import router as feed_ai_router
from app.api.routes.health import router as health_router
from app.api.routes.linkedin import router as linkedin_router
from app.api.routes.feed_batch import router as feed_batch_router
from app.api.routes.digest import router as digest_router
from app.scheduler.digest_scheduler import scheduler
from app.api.routes.suggest_replies import router as suggest_reply_router

app = FastAPI(title="Veera Backend")
scheduler.start()


app.include_router(health_router)
app.include_router(linkedin_router, prefix="/linkedin")


@app.get("/")
def root():
    return {
        "message": "Veera Backend Running"
    }

app.include_router(
    feed_ai_router,
    prefix="/linkedin"
)

app.include_router(
    feed_batch_router,
    prefix="/linkedin"
)

app.include_router(
    digest_router,
    prefix="/linkedin"
)

app.include_router(
    suggest_reply_router,
    prefix="/linkedin"
)