from pydantic import BaseModel, ConfigDict


class TaskBase(BaseModel):
	title: str
	description: str | None = None


class TaskCreate(TaskBase):
	pass


class TaskResponse(TaskBase):
	id: int
	completed: bool = False

	model_config = ConfigDict(from_attributes=True)
