from pydantic import BaseModel

from statements.domain.validation_types import ProjectName

class Veto(BaseModel):
    id_: str
    project: ProjectName
    description: str
