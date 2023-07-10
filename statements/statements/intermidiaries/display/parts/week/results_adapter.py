from statements.domain.progress_status import ProgressStatus
from statements.domain.statements.week_statement import WeeklyStatement
from statements.intermidiaries.display.context.adapter import ContextAdapter
from statements.intermidiaries.display.habits.maintenance_adapter import HabitMaintenanceAdapter
from statements.intermidiaries.display.incidents.adapter import IncidentAdapter
from statements.intermidiaries.display.issue.adapter import IssueAdapter
from statements.intermidiaries.display.parts.week.results import DisplayWeekResults
from statements.intermidiaries.display.proposals.adapter import ProposalAdapter
from statements.intermidiaries.display.tasks.adapter import TaskAdapter
from statements.intermidiaries.display.vetoes.maintenance_adapter import VetoMaintenanceAdapter


class WeekResultsAdapter:
    def __init__(self, incident_adapter: IncidentAdapter, context_adapter: ContextAdapter,
                 habit_maintenance_adapter: HabitMaintenanceAdapter,
                 veto_maintenance_adapter: VetoMaintenanceAdapter,
                 task_adapter: TaskAdapter,
                 issue_adapter: IssueAdapter,
                 proposal_adapter: ProposalAdapter):
        self.incident_adapter = incident_adapter
        self.context_adapter = context_adapter
        self.habit_maintenance_adapter = habit_maintenance_adapter
        self.veto_maintenance_adapter = veto_maintenance_adapter
        self.task_adapter = task_adapter
        self.issue_adapter = issue_adapter
        self.proposal_adapter = proposal_adapter

    def get_display_results(self, statement: WeeklyStatement) -> DisplayWeekResults:
        return DisplayWeekResults(
            incidents=[self.incident_adapter.get_display_incident(incident, statement.projects_to_aspects)
                       for incident in statement.incidents],
            new_context=[self.context_adapter.get_display_context(context, statement.projects_to_aspects)
                         for context in statement.new_context],
            habit_maintenance=[
                self.habit_maintenance_adapter.get_display_maintenance(maintenance, statement.projects_to_aspects)
                for maintenance in statement.habit_maintenance],
            veto_maintenance=[
                self.veto_maintenance_adapter.get_display_veto_maintenance(veto_maintenance,
                                                                           statement.projects_to_aspects)
                for veto_maintenance in statement.veto_maintenance
            ],
            resolved_tasks=[
                self.task_adapter.get_display_task(task, statement.projects_to_aspects)
                for task in statement.tasks
                if task.status in [ProgressStatus.DONE, ProgressStatus.FAILED]
            ],
            resolved_proposals=[
                self.proposal_adapter.get_display_proposal(proposal, statement.projects_to_aspects)
                for proposal in statement.proposals
                if proposal.accepted is not None
            ],
            new_issues=[
                self.issue_adapter.get_display_issue(issue, statement.projects_to_aspects)
                for issue in statement.new_issues
            ],
            closed_issues=[
                self.issue_adapter.get_display_issue(issue, statement.projects_to_aspects)
                for issue in statement.closed_issues
            ],
        )
