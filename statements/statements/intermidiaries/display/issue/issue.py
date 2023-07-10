from pydantic import BaseModel

from statements.domain.validation_types import Markdown
from statements.intermidiaries.display.projects.project import DisplayProject


class DisplayIssue(BaseModel):
    project: DisplayProject
    id_: str
    title: str
    description: Markdown | None
    note: Markdown | None
