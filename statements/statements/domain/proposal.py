from pydantic import BaseModel

from statements.domain.validation_types import ProjectName

class Proposal(BaseModel):
    project: ProjectName
    description: str
    accepted: bool | None = None
