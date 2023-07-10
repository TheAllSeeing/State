from pydantic import BaseModel

from statements.domain.validation_types import ProjectName

class Event(BaseModel):
    time: str
    project: ProjectName
    description: str
