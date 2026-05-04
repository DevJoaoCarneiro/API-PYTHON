from fastapi import APIRouter, Depends, Response, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.task_schema import TaskCreate, TaskResponse
from app.services.task_service import create_task as create_task_service
from app.services.task_service import delete_task as delete_task_service
from app.services.task_service import get_task_by_id as get_task_by_id_service
from app.services.task_service import list_tasks as list_tasks_service

router = APIRouter()


@router.post("/", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
def create_task(task_data: TaskCreate, db: Session = Depends(get_db)):
	return create_task_service(db, task_data)


@router.get("/", response_model=list[TaskResponse])
def list_tasks(db: Session = Depends(get_db)):
	return list_tasks_service(db)


@router.get("/{task_id}", response_model=TaskResponse)
def get_task_by_id(task_id: int, db: Session = Depends(get_db)):
	return get_task_by_id_service(db, task_id)


@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int, db: Session = Depends(get_db)) -> Response:
	delete_task_service(db, task_id)
	return Response(status_code=status.HTTP_204_NO_CONTENT)

