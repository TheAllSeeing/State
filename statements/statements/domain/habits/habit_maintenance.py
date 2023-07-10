from collections import OrderedDict

from pydantic import BaseModel, RootModel

from statements.domain.habits.habit import Habit
from statements.domain.progress_status import ProgressStatus


class SeriesMaintenance(RootModel):
    root: OrderedDict[str, ProgressStatus]


class ScopeSeriesMaintenance(RootModel):
    root: OrderedDict[str, SeriesMaintenance]


class HabitMaintenance(BaseModel):
    habit: Habit
    maintenance: ScopeSeriesMaintenance | SeriesMaintenance

#
# Scope = str
# Count = int
#
#
# class HabitMaintenance(BaseModel):
#     expected: list[date] | dict[Scope, Count]
#     actual: list[date]
