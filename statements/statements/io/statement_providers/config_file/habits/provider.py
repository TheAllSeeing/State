from abc import ABC, abstractmethod

from statements.domain.habits.habit import Habit, HabitFrequency
from statements.io.statement_providers.config_file.habits.habit import HabitConfig
from statements.io.statement_providers.config_file.toml_provider import TOMLProvider


class HabitsProvider(ABC):
    @abstractmethod
    def get_habits(self) -> list[Habit]:
        pass


class TOMLHabitProvider(HabitsProvider, TOMLProvider):
    def get_habits(self) -> list[Habit]:
        raw_habits = self._get_raw_data()
        config_habits = HabitConfig.model_validate(raw_habits)

        return [Habit(
            id_=habit.id_,
            frequency=HabitFrequency(scope=scope, count=habit.frequency.count, hop=habit.frequency.hop),
            project=project,
            description=habit.description,
        ) for scope, scope_habits in config_habits
            for project, project_habits in scope_habits.items()
            for habit in project_habits
        ]
