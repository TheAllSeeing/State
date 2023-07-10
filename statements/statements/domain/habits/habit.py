from enum import Enum

from pydantic import BaseModel

from statements.domain.validation_types import ProjectName

class HabitScope(Enum):
    DAILY = 'daily'
    WEEKLY = 'weekly'
    MONTHLY = 'monthly'


class HabitFrequency(BaseModel):
    scope: HabitScope
    count: int | None = None
    hop: int | None = None


class Habit(BaseModel):
    id_: str
    frequency: HabitFrequency
    project: ProjectName
    description: str
