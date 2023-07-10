from pydantic import BaseModel

from statements.intermidiaries.display.projects.project import DisplayProject


class DisplayIncident(BaseModel):
    id_: str
    project: DisplayProject
    title: str
    description: str
