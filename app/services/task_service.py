from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.repositories.task_repository import create_task as repo_create_task
from app.repositories.task_repository import delete_task as repo_delete_task
from app.repositories.task_repository import get_task_by_id as repo_get_task_by_id
from app.repositories.task_repository import list_tasks as repo_list_tasks
from app.schemas.task_schema import TaskCreate


def create_task(db: Session, task_data: TaskCreate):
	return repo_create_task(db, task_data)


def list_tasks(db: Session):
	return repo_list_tasks(db)


def get_task_by_id(db: Session, task_id: int):
	task = repo_get_task_by_id(db, task_id)
	if task is None:
		raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
	return task


def delete_task(db: Session, task_id: int) -> None:
	task = get_task_by_id(db, task_id)
	repo_delete_task(db, task)
