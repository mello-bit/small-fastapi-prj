from sqlmodel import SQLModel, Field
from typing import Optional, List


# SQLModel базируется на pydantic, и с ним удобнее работать с бд
class Task(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True, nullable=False)
    name: str = Field(default="", nullable=False)
    description: str = Field(default="", max_length=200)
    completed: bool = Field(default=False, nullable=False)


class UpdateTask(SQLModel):
    name: str = Field(default="", nullable=False)
    description: str = Field(default="", max_length=200)
    completed: bool = Field(default=False, nullable=False)


class TasksList(SQLModel):
    tasks: List[Task]
    count: int
