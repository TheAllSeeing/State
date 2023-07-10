from pydantic import BaseModel

from statements.intermidiaries.display.events.event import DisplayEvent
from statements.intermidiaries.display.goals.goal import DisplayGoal
from statements.intermidiaries.display.habits.habit import DisplayHabit
from statements.intermidiaries.display.vetoes.veto import DisplayVeto


class DisplayMonthOutline(BaseModel):
    schedule: list[DisplayEvent]
    goals: list[DisplayGoal]
    habits: list[DisplayHabit]
    vetoes: list[DisplayVeto]
    plan: list[DisplayEvent]
