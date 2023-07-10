from statements.domain.events.event import Event
from statements.domain.long_goals.goal_closure import LongGoalClosure
from statements.domain.long_goals.long_goal import LongGoal
from statements.domain.habits.habit import Habit
from statements.domain.habits.habit_maintenance import HabitMaintenance
from statements.domain.incidents.context import ContextItem
from statements.domain.incidents.incident import Incident
from statements.domain.issue import Issue
from statements.domain.project_status_change import ProjectStatusChange
from statements.domain.proposal import Proposal
from statements.domain.statements.base_statement import Statement
from statements.domain.validation_types import Markdown
from statements.domain.vetoes.veto import Veto
from statements.domain.vetoes.veto_maintenance import VetoMaintenance


class SeasonStatement(Statement):
    overview: Markdown
    goals: list[LongGoal]
    proposals: list[Proposal]
    schedule: list[Event]
    habits: list[Habit]
    vetoes: list[Veto]
    timeline: list[Event]
    issues: list[Issue]
    incidents: list[Incident]
    new_context: list[ContextItem]
    veto_maintenance: list[VetoMaintenance]
    new_issues: list[Issue]
    closed_issues: list[Issue]
    project_status_changes: list[ProjectStatusChange]
    new_goals: list[LongGoal]
    goal_closures: list[LongGoalClosure]
    new_proposals: list[Proposal]
    notes: Markdown
