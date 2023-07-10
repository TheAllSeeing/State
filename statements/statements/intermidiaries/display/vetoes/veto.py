from pydantic import BaseModel

from statements.intermidiaries.display.projects.project import DisplayProject


class DisplayVeto(BaseModel):
    project: DisplayProject
    description: str
