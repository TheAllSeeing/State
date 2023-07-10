
from statements.domain.statements.day_statement import DailyStatement
from statements.io.statement_providers.config_file.context.context import ContextProvider
from statements.io.statement_providers.config_file.day.provider import DayProvider
from statements.io.statement_providers.config_file.events.timeline_provider import TimelineProvider
from statements.io.statement_providers.config_file.goals.goals_provider import GoalsProvider
from statements.io.statement_providers.config_file.habits.maintenance_provider import HabitMaintenanceProvider
from statements.io.statement_providers.config_file.habits.provider import HabitsProvider
from statements.io.statement_providers.config_file.incidents.provider import IncidentsProvider
from statements.io.statement_providers.config_file.issues.provider import IssuesProvider
from statements.io.statement_providers.config_file.long_goals.overview import MarkdownProvider
from statements.io.statement_providers.config_file.proposals.provider import ProposalsProvider
from statements.io.statement_providers.config_file.settings.aspects_provider import AspectsProvider
from statements.io.statement_providers.config_file.settings.settings_provider import StatementSettingsProvider
from statements.io.statement_providers.config_file.tasks.tasks_provider import TasksProvider
from statements.io.statement_providers.config_file.vetoes.maintenance_provider import VetoMaintenanceProvider
from statements.io.statement_providers.config_file.vetoes.provider import VetoesProvider
from statements.use_cases.ports.statement_provider import StatementProvider


class FilesDailyStatementProvider(StatementProvider):
    def __init__(self, settings_provider: StatementSettingsProvider, aspects_provider: AspectsProvider,
                 schedule_provider: TimelineProvider,
                 tasks_provider: TasksProvider,
                 proposals_provider: ProposalsProvider,
                 vetoes_provider: VetoesProvider,
                 plan_provider: TimelineProvider, issues_provider: IssuesProvider,
                 day_provider: DayProvider,
                 incidents_provider: IncidentsProvider, context_provider: ContextProvider,
                 new_issues_provider: IssuesProvider,
                 new_tasks_provider: TasksProvider,
                 new_proposals_provider: ProposalsProvider,
                 notes_provider: MarkdownProvider):
        self.settings_provider = settings_provider
        self.aspects_provider = aspects_provider
        self.schedule_provider = schedule_provider
        self.tasks_provider = tasks_provider
        self.vetoes_provider = vetoes_provider
        self.day_provider = day_provider
        self.plan_provider = plan_provider
        self.proposals_provider = proposals_provider
        self.issues_provider = issues_provider
        self.incidents_provider = incidents_provider
        self.context_provider = context_provider
        self.new_issues_provider = new_issues_provider
        self.new_tasks_provider = new_tasks_provider
        self.new_proposals_provider = new_proposals_provider
        self.notes_provider = notes_provider

    def get_statement(self) -> DailyStatement:
        issues = self.issues_provider.get_issues()
        settings = self.settings_provider.get_statement_settings()
        day = self.day_provider.get_day(statement_date=settings.scope.start)

        return DailyStatement(
            config=settings,
            aspects=self.aspects_provider.get_aspects(),
            schedule=self.schedule_provider.get_timeline(),
            tasks=self.tasks_provider.get_tasks(),
            vetoes=self.vetoes_provider.get_vetoes(),
            timeline=self.plan_provider.get_timeline(),
            issues=issues.open,
            diary=day.diary,
            sleep=day.sleep,
            rest=day.rest,
            proposals=self.proposals_provider.get_proposals(),
            incidents=self.incidents_provider.get_incidents(),
            new_context=self.context_provider.get_context_items(),
            new_issues=self.new_issues_provider.get_issues().open,
            closed_issues=issues.resolved,
            new_tasks=self.new_tasks_provider.get_tasks(),
            new_proposals=self.new_proposals_provider.get_proposals(),
            notes=self.notes_provider.get_markdown()
        )
