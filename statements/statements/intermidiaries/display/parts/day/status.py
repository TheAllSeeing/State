from pydantic import BaseModel

from statements.intermidiaries.display.goals.goal import DisplayGoal
from statements.intermidiaries.display.issue.issue import DisplayIssue
from statements.intermidiaries.display.proposals.proposal import DisplayProposal
from statements.intermidiaries.display.tasks.task import DisplayTask


class DisplayDayStatus(BaseModel):
    issues: list[DisplayIssue]
    open_tasks: list[DisplayTask]
    open_proposals: list[DisplayProposal]
