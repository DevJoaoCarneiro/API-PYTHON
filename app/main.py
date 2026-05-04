from fastapi import FastAPI

from app.controllers.task_controller import router as task_router
from app.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Todo API", version="0.1.0")

app.include_router(task_router, prefix="/tasks", tags=["tasks"])


@app.get("/")
def health_check() -> dict:
	return {"status": "ok"}
