from pydantic import BaseModel

from statements.domain.validation_types import Markdown
from statements.intermidiaries.display.goals.goal_closure import DisplayGoalClosure
from statements.intermidiaries.display.goals.goal import DisplayGoal
from statements.intermidiaries.display.proposals.proposal import DisplayProposal


class DisplayMonthConclusions(BaseModel):
    new_goals: list[DisplayGoal]
    closed_goals: list[DisplayGoalClosure]
    new_proposals: list[DisplayProposal]
    notes: Markdown
