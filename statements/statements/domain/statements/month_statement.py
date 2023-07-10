from statements.domain.events.event import Event
from statements.domain.goals.goal import Goal
from statements.domain.goals.goal_closure import GoalClosure
from statements.domain.habits.habit import Habit
from statements.domain.habits.habit_maintenance import HabitMaintenance
from statements.domain.incidents.context import ContextItem
from statements.domain.incidents.incident import Incident
from statements.domain.issue import Issue
from statements.domain.proposal import Proposal
from statements.domain.statements.base_statement import Statement
from statements.domain.validation_types import Markdown
from statements.domain.vetoes.veto import Veto
from statements.domain.vetoes.veto_maintenance import VetoMaintenance


class MonthlyStatement(Statement):
    schedule: list[Event]
    goals: list[Goal]
    habits: list[Habit]
    vetoes: list[Veto]
    proposals: list[Proposal]
    timeline: list[Event]
    issues: list[Issue]
    incidents: list[Incident]
    new_context: list[ContextItem]
    habit_maintenance: list[HabitMaintenance]
    veto_maintenance: list[VetoMaintenance]
    new_issues: list[Issue]
    closed_issues: list[Issue]
    new_goals: list[Goal]
    goal_closures: list[GoalClosure]
    new_proposals: list[Proposal]
    notes: Markdown

