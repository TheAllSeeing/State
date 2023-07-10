from pydantic import BaseModel

from statements.intermidiaries.display.color.color import DisplayColor


class DisplayProject(BaseModel):
    color: DisplayColor
    name: str