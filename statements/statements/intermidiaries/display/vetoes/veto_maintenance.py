from pydantic import BaseModel

from statements.intermidiaries.display.projects.project import DisplayProject


class DisplayVetoViolation(BaseModel):
    time_point: str
    detail: str


class DisplayVetoMaintenance(BaseModel):
    project: DisplayProject
    title: str
    violations: list[DisplayVetoViolation]
