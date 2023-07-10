from pydantic import BaseModel

from statements.intermidiaries.display.long_goals.long_goal import DisplayLongGoal
from statements.intermidiaries.display.issue.issue import DisplayIssue
from statements.intermidiaries.display.proposals.proposal import DisplayProposal


class DisplaySeasonStatus(BaseModel):
    issues: list[DisplayIssue]
    goals: list[DisplayLongGoal]
    open_proposals: list[DisplayProposal]
