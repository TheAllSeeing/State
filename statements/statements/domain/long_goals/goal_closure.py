from pydantic import BaseModel

from statements.domain.long_goals.long_goal import LongGoal


class LongGoalClosure(BaseModel):
    goal: LongGoal
    reason: str
