from pydantic import BaseModel

from statements.domain.outline.outline import Markdown
from statements.io.latex.models.event import LatexEvent
from statements.io.latex.models.long_goal import LatexLongGoal


class LatexOutline(BaseModel):
    overview: Markdown
    schedule: list[LatexEvent]
    goals: list[LatexLongGoal]
