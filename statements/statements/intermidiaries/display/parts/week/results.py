from pydantic import BaseModel

from statements.intermidiaries.display.context.context import DisplayContextItem
from statements.intermidiaries.display.habits.habit_maintenance import DisplayScopeMaintenance, DisplaySeriesMaintenance
from statements.intermidiaries.display.incidents.incident import DisplayIncident
from statements.intermidiaries.display.issue.issue import DisplayIssue
from statements.intermidiaries.display.proposals.proposal import DisplayProposal
from statements.intermidiaries.display.tasks.task import DisplayTask
from statements.intermidiaries.display.vetoes.veto_maintenance import DisplayVetoMaintenance


class DisplayWeekResults(BaseModel):
    incidents: list[DisplayIncident]
    new_context: list[DisplayContextItem]
    habit_maintenance: list[DisplayScopeMaintenance | DisplaySeriesMaintenance]
    veto_maintenance: list[DisplayVetoMaintenance]
    resolved_tasks: list[DisplayTask]
    resolved_proposals: list[DisplayProposal]
    new_issues: list[DisplayIssue]
    closed_issues: list[DisplayIssue]
