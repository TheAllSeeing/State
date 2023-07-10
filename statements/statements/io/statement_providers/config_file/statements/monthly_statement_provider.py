
from statements.domain.statements.month_statement import MonthlyStatement
from statements.io.statement_providers.config_file.context.context import ContextProvider
from statements.io.statement_providers.config_file.events.timeline_provider import TimelineProvider
from statements.io.statement_providers.config_file.goals.goal_conclusions_provider import GoalConclusionsProvider
from statements.io.statement_providers.config_file.goals.goals_provider import GoalsProvider
from statements.io.statement_providers.config_file.habits.maintenance_provider import HabitMaintenanceProvider
from statements.io.statement_providers.config_file.habits.provider import HabitsProvider
from statements.io.statement_providers.config_file.incidents.provider import IncidentsProvider
from statements.io.statement_providers.config_file.issues.provider import IssuesProvider
from statements.io.statement_providers.config_file.long_goals.overview import MarkdownProvider
from statements.io.statement_providers.config_file.proposals.provider import ProposalsProvider
from statements.io.statement_providers.config_file.settings.aspects_provider import AspectsProvider
from statements.io.statement_providers.config_file.settings.settings_provider import StatementSettingsProvider
from statements.io.statement_providers.config_file.vetoes.maintenance_provider import VetoMaintenanceProvider
from statements.io.statement_providers.config_file.vetoes.provider import VetoesProvider
from statements.use_cases.ports.statement_provider import StatementProvider


class FilesMonthlyStatementProvider(StatementProvider):
    def __init__(self, settings_provider: StatementSettingsProvider, aspects_provider: AspectsProvider,
                 schedule_provider: TimelineProvider,
                 habits_provider: HabitsProvider, vetoes_provider: VetoesProvider,
                 goals_provider: GoalsProvider,
                 proposals_provider: ProposalsProvider,
                 plan_provider: TimelineProvider, issues_provider: IssuesProvider,
                 incidents_provider: IncidentsProvider, context_provider: ContextProvider,
                 habit_maintenance_provider: HabitMaintenanceProvider,
                 veto_maintenance_provider: VetoMaintenanceProvider,
                 new_issues_provider: IssuesProvider,
                 goal_conclusions_provider: GoalConclusionsProvider,
                 new_proposals_provider: ProposalsProvider,
                 notes_provider: MarkdownProvider):
        self.settings_provider = settings_provider
        self.aspects_provider = aspects_provider
        self.schedule_provider = schedule_provider
        self.goals_provider = goals_provider
        self.habits_provider = habits_provider
        self.vetoes_provider = vetoes_provider
        self.plan_provider = plan_provider
        self.proposals_provider = proposals_provider
        self.issues_provider = issues_provider
        self.incidents_provider = incidents_provider
        self.context_provider = context_provider
        self.habit_maintenance_provider = habit_maintenance_provider
        self.veto_maintenance_provider = veto_maintenance_provider
        self.new_issues_provider = new_issues_provider
        self.goal_conclusions_provider = goal_conclusions_provider
        self.new_proposals_provider = new_proposals_provider
        self.notes_provider = notes_provider

    def get_statement(self) -> MonthlyStatement:
        habits = self.habits_provider.get_habits()
        vetoes = self.vetoes_provider.get_vetoes()
        issues = self.issues_provider.get_issues()
        goals = self.goals_provider.get_goals()
        goal_conclusions = self.goal_conclusions_provider.get_goal_conclusions(outline_goals={goal.id_: goal
                                                                                              for goal in goals})
        return MonthlyStatement(
            config=self.settings_provider.get_statement_settings(),
            aspects=self.aspects_provider.get_aspects(),
            schedule=self.schedule_provider.get_timeline(),
            goals=goals,
            habits=habits,
            vetoes=vetoes,
            timeline=self.plan_provider.get_timeline(),
            issues=issues.open,
            proposals=self.proposals_provider.get_proposals(),
            incidents=self.incidents_provider.get_incidents(),
            new_context=self.context_provider.get_context_items(),
            habit_maintenance=self.habit_maintenance_provider.get_habit_maintenance(habits={habit.id_: habit
                                                                                            for habit in habits}),
            veto_maintenance=self.veto_maintenance_provider.get_veto_maintenance(vetoes={veto.id_: veto for veto
                                                                                         in vetoes}),
            new_issues=self.new_issues_provider.get_issues().open,
            closed_issues=issues.resolved,
            new_goals=goal_conclusions.new_goals,
            goal_closures=goal_conclusions.goal_closures,
            new_proposals=self.new_proposals_provider.get_proposals(),
            notes=self.notes_provider.get_markdown()
        )
