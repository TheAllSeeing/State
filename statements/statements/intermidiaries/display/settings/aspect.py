from pydantic import BaseModel

from statements.intermidiaries.display.color.color import DisplayColor
from statements.intermidiaries.display.projects.project import DisplayProject


class DisplayAspect(BaseModel):
    name: str
    color: DisplayColor
    active_projects: list[DisplayProject]
    passive_projects: list[DisplayProject]
    frozen_projects: list[DisplayProject]
    archived_projects: list[DisplayProject]
