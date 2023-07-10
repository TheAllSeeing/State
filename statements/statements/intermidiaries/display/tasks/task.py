from pydantic import BaseModel

from statements.domain.validation_types import Markdown
from statements.intermidiaries.display.progress_status.progress_status import DisplayProgressStatus
from statements.intermidiaries.display.projects.project import DisplayProject


class DisplayTask(BaseModel):
    id_: str
    project: DisplayProject
    description: Markdown
    status: DisplayProgressStatus
    note: str | None
