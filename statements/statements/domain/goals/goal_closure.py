from pydantic import BaseModel

from statements.domain.goals.goal import Goal


class GoalClosure(BaseModel):
    goal: Goal
    reason: str
