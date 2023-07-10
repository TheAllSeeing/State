from pydantic import BaseModel

from statements.intermidiaries.display.goals.goal import DisplayGoal


class DisplayGoalClosure(BaseModel):
    goal: DisplayGoal
    reason: str
