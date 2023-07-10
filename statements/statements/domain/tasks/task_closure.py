from pydantic import BaseModel

from statements.domain.tasks.task import Task


class TaskClosure(BaseModel):
    task: Task
    reason: str
