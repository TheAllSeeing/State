from statements.domain.day import Diary, Sleep, RestItem
from statements.domain.events.event import Event
from statements.domain.incidents.context import ContextItem
from statements.domain.incidents.incident import Incident
from statements.domain.issue import Issue
from statements.domain.proposal import Proposal
from statements.domain.statements.base_statement import Statement
from statements.domain.tasks.task import Task
from statements.domain.validation_types import Markdown
from statements.domain.vetoes.veto import Veto


class DailyStatement(Statement):
    schedule: list[Event]
    tasks: list[Task]
    vetoes: list[Veto]
    proposals: list[Proposal]
    timeline: list[Event]
    issues: list[Issue]
    diary: Diary
    sleep: Sleep
    rest: list[RestItem]
    incidents: list[Incident]
    new_context: list[ContextItem]
    new_issues: list[Issue]
    closed_issues: list[Issue]
    new_tasks: list[Task]
    new_proposals: list[Proposal]
    notes: Markdown
