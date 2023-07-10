from enum import Enum

from pydantic import BaseModel

from statements.intermidiaries.display.projects.project import DisplayProject


class DisplayStatusChange(Enum):
    NEW = 'New'
    THAWED = 'Thawed'
    FROZEN = 'Frozen'
    CLOSED = 'Closed'


class DisplayProjectStatusChange(BaseModel):
    project: DisplayProject
    project_stub: str
    change_description: str
