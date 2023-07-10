from pydantic import BaseModel

from statements.domain.validation_types import Markdown
from statements.domain.validation_types import ProjectName

class Issue(BaseModel):
    id_: str
    project: ProjectName
    title: str
    description: Markdown | None
    note: Markdown | None
