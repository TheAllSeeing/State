from statements.domain.progress_status import ProgressStatus
from statements.domain.statements.day_statement import DailyStatement
from statements.intermidiaries.display.context.adapter import ContextAdapter
from statements.intermidiaries.display.day.adapter import DiaryAdapter, SleepAdapter, RestAdapter
from statements.intermidiaries.display.habits.maintenance_adapter import HabitMaintenanceAdapter
from statements.intermidiaries.display.incidents.adapter import IncidentAdapter
from statements.intermidiaries.display.issue.adapter import IssueAdapter
from statements.intermidiaries.display.parts.day.results import DisplayDayResults
from statements.intermidiaries.display.proposals.adapter import ProposalAdapter
from statements.intermidiaries.display.tasks.adapter import TaskAdapter
from statements.intermidiaries.display.vetoes.maintenance_adapter import VetoMaintenanceAdapter


class DayResultsAdapter:
    def __init__(self, incident_adapter: IncidentAdapter, context_adapter: ContextAdapter,
                 diary_adapter: DiaryAdapter,
                 sleep_adapter: SleepAdapter,
                 rest_adapter: RestAdapter,
                 task_adapter: TaskAdapter,
                 issue_adapter: IssueAdapter,
                 proposal_adapter: ProposalAdapter):
        self.incident_adapter = incident_adapter
        self.context_adapter = context_adapter
        self.diary_adapter = diary_adapter
        self.sleep_adapter = sleep_adapter
        self.rest_adapter = rest_adapter
        self.task_adapter = task_adapter
        self.issue_adapter = issue_adapter
        self.proposal_adapter = proposal_adapter

    def get_display_results(self, statement: DailyStatement) -> DisplayDayResults:
        return DisplayDayResults(
            incidents=[self.incident_adapter.get_display_incident(incident, statement.projects_to_aspects)
                       for incident in statement.incidents],
            new_context=[self.context_adapter.get_display_context(context, statement.projects_to_aspects)
                         for context in statement.new_context],
            diary=self.diary_adapter.get_display_diary(statement.diary, statement.config.scope.start),
            sleep=self.sleep_adapter.get_display_sleep(statement.sleep, statement.config.scope.start),
            rest=[self.rest_adapter.get_display_rest_item(rest_item)
                  for rest_item in statement.rest],
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
