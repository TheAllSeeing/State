from enum import Enum

from pydantic import BaseModel

from statements.domain.validation_types import ProjectName


class StatusChange(Enum):
    NEW = 'new'
    THAWED = 'thawed'
    FROZEN = 'frozen'
    CLOSED = 'closed'


class ProjectStatusChange(BaseModel):
    project: ProjectName
    status_change: StatusChange
    project_stub: str
    change_description: str
