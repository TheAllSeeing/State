from pydantic import BaseModel

from statements.domain.validation_types import ProjectName

class ContextItem(BaseModel):
    project: ProjectName
    description: str
