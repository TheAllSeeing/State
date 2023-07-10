from pydantic import BaseModel

from statements.domain.progress_status import ProgressStatus


class Goal(BaseModel):
    id_: str
    project: str
    description: str
    note: str | None
    status: ProgressStatus
