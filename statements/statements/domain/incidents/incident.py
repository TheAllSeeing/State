from pydantic import BaseModel

from statements.domain.validation_types import ProjectName

class Incident(BaseModel):
    id_: str
    project: ProjectName
    title: str
    description: str
