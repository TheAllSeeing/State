from pydantic import BaseModel

from statements.intermidiaries.display.context.context import DisplayContextItem
from statements.intermidiaries.display.day.day import DisplayDiary, DisplaySleep, DisplayRest
from statements.intermidiaries.display.incidents.incident import DisplayIncident
from statements.intermidiaries.display.issue.issue import DisplayIssue
from statements.intermidiaries.display.proposals.proposal import DisplayProposal
from statements.intermidiaries.display.tasks.task import DisplayTask


class DisplayDayResults(BaseModel):
    incidents: list[DisplayIncident]
    new_context: list[DisplayContextItem]
    diary: DisplayDiary
    sleep: DisplaySleep
    rest: DisplayRest
    resolved_tasks: list[DisplayTask]
    resolved_proposals: list[DisplayProposal]
    new_issues: list[DisplayIssue]
    closed_issues: list[DisplayIssue]
