from sqlalchemy.orm import Session

from app.models.task_model import Task
from app.schemas.task_schema import TaskCreate


def create_task(db: Session, task_data: TaskCreate) -> Task:
	task = Task(**task_data.model_dump())
	db.add(task)
	db.commit()
	db.refresh(task)
	return task


def list_tasks(db: Session) -> list[Task]:
	return db.query(Task).all()


def get_task_by_id(db: Session, task_id: int) -> Task | None:
	return db.query(Task).filter(Task.id == task_id).first()


def delete_task(db: Session, task: Task) -> None:
	db.delete(task)
	db.commit()
