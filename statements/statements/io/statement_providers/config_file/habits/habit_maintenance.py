from pydantic import RootModel
from typing_extensions import TypeAlias

from statements.io.statement_providers.config_file.progress_status.progress_status import InputProgressStatus

ID: TypeAlias = str
Scope: TypeAlias = str
Item: TypeAlias = str


InputScopeHabitMaintenance = RootModel[dict[Scope, dict[Item, InputProgressStatus]]]
InputSeriesHabitMaintenance = RootModel[dict[Item, InputProgressStatus]]
InputHabitMaintenance = RootModel[dict[ID, InputScopeHabitMaintenance | InputSeriesHabitMaintenance]]
