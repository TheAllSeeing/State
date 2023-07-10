from pydantic import BaseModel

from statements.domain.validation_types import Markdown
from statements.intermidiaries.display.events.event import DisplayEvent
from statements.intermidiaries.display.habits.habit import DisplayHabit
from statements.intermidiaries.display.long_goals.long_goal import DisplayLongGoal
from statements.intermidiaries.display.vetoes.veto import DisplayVeto


class DisplaySeasonOutline(BaseModel):
    overview: Markdown
    schedule: list[DisplayEvent]
    goals: list[DisplayLongGoal]
    habits: list[DisplayHabit]
    vetoes: list[DisplayVeto]
    plan: list[DisplayEvent]
