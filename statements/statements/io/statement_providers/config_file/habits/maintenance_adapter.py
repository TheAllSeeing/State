from statements.domain.habits.habit_maintenance import ScopeSeriesMaintenance, SeriesMaintenance
from statements.io.statement_providers.config_file.progress_status.adapter import InputProgressStatusAdapter
from statements.io.statement_providers.config_file.habits.habit_maintenance import InputScopeHabitMaintenance, InputSeriesHabitMaintenance


class InputHabitMaintenanceAdapter:
    def __init__(self, status_adapter: InputProgressStatusAdapter):
        self.status_adapter = status_adapter

    def get_habit_maintenance_data(self,
                                   input_maintenance_data: InputScopeHabitMaintenance | InputSeriesHabitMaintenance) \
            -> ScopeSeriesMaintenance | SeriesMaintenance:
        if isinstance(input_maintenance_data, InputScopeHabitMaintenance):
            return {scope: {item: self.status_adapter.get_progress_status(status)
                            for item, status in item_data.items()}
                    for scope, item_data in input_maintenance_data.root.items()}
        if isinstance(input_maintenance_data, InputSeriesHabitMaintenance):
            return {scope: self.status_adapter.get_progress_status(status)
                    for scope, status in input_maintenance_data.root.items()}
        else:
            raise NotImplementedError(
                f'Unrecognized maintenance data type: {input_maintenance_data.__class__.__name__}')
