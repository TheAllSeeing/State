from pydantic import BaseModel

from statements.domain.validation_types import Markdown
from statements.intermidiaries.display.color.color import DisplayColor
from statements.intermidiaries.display.progress_status.progress_status import DisplayProgressStatus


class DisplayLongGoal(BaseModel):
    id_: str
    color: DisplayColor
    projects: str
    description: Markdown
    status: DisplayProgressStatus
    note: str | None
