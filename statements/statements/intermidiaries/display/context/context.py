from pydantic import BaseModel

from statements.intermidiaries.display.projects.project import DisplayProject


class DisplayContextItem(BaseModel):
    project: DisplayProject
    description: str
