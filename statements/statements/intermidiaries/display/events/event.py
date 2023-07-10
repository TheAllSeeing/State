from pydantic import BaseModel

from statements.intermidiaries.display.projects.project import DisplayProject


class DisplayEvent(BaseModel):
    time: str
    project: DisplayProject
    description: str
