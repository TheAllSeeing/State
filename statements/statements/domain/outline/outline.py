from typing import TypeVar

from pydantic import BaseModel

from statements.domain.outline.event import Event
from statements.domain.outline.long_goal import LongGoal

Markdown = TypeVar('Markdown', bound=str)


class Outline(BaseModel):
    overview: Markdown
    schedule: list[Event]
    goals: list[LongGoal]
