from abc import ABC, abstractmethod
from pathlib import Path

from statements.domain.habits.habit import Habit
from statements.domain.habits.habit_maintenance import HabitMaintenance
from statements.io.statement_providers.config_file.habits.maintenance_adapter import InputHabitMaintenanceAdapter
from statements.io.statement_providers.config_file.habits.habit_maintenance import InputHabitMaintenance
from statements.io.statement_providers.config_file.toml_provider import TOMLProvider


class HabitMaintenanceProvider(ABC):
    @abstractmethod
    def get_habit_maintenance(self, habits: dict[str, Habit]) -> list[HabitMaintenance]:
        pass


class TOMLHabitMaintenanceProvider(HabitMaintenanceProvider, TOMLProvider):
    def __init__(self, file_path: Path, maintenance_adapter: InputHabitMaintenanceAdapter):
        super().__init__(file_path)
        self.maintenance_adapter = maintenance_adapter

    def get_habit_maintenance(self, habits: dict[str, Habit]) -> list[HabitMaintenance]:
        raw_data = self._get_raw_data()
        parsed_data = InputHabitMaintenance.model_validate(raw_data).root
        result = []
        for habit_id, maintenance in parsed_data.items():
            try:
                habit = habits[habit_id]
            except KeyError:
                raise ValueError(f'Failed to find habit of habit maintenance: no such habit {habit_id}')

            result.append(HabitMaintenance(
                habit=habit,
                maintenance=self.maintenance_adapter.get_habit_maintenance_data(maintenance)
            ))
        return result
