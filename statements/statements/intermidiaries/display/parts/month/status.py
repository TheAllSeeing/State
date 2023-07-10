from pydantic import BaseModel

from statements.intermidiaries.display.goals.goal import DisplayGoal
from statements.intermidiaries.display.issue.issue import DisplayIssue
from statements.intermidiaries.display.proposals.proposal import DisplayProposal


class DisplayMonthStatus(BaseModel):
    issues: list[DisplayIssue]
    goals: list[DisplayGoal]
    open_proposals: list[DisplayProposal]
