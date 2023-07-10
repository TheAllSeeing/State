from pydantic import BaseModel

from statements.domain.progress_status import ProgressStatus


class LongGoal(BaseModel):
    id_: str
    projects: list[str]
    description: str
    note: str | None
    status: ProgressStatus
