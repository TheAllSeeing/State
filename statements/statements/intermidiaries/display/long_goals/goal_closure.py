from pydantic import BaseModel

from statements.intermidiaries.display.long_goals.long_goal import DisplayLongGoal


class DisplayLongGoalClosure(BaseModel):
    goal: DisplayLongGoal
    reason: str
