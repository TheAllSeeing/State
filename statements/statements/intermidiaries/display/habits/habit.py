from typing import Annotated

from pydantic import BaseModel
from pydantic.functional_validators import AfterValidator

from statements.intermidiaries.display.projects.project import DisplayProject

Frequency = Annotated[str, AfterValidator(str.title)]


class DisplayHabit(BaseModel):
    id_: str
    project: DisplayProject
    description: str
    frequency: Frequency
    count: int | None = None
    hop: int | None = None
