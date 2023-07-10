from abc import ABC, abstractmethod
from pathlib import Path

from statements.domain.tasks.task import Task
from statements.io.statement_providers.config_file.tasks.adapter import InputTaskAdapter
from statements.io.statement_providers.config_file.progress_status.adapter import InputProgressStatusAdapter
from statements.io.statement_providers.config_file.tasks.task import InputTasks
from statements.io.statement_providers.config_file.toml_provider import TOMLProvider


class TasksProvider(ABC):
    @abstractmethod
    def get_tasks(self) -> list[Task]:
        pass


class TOMLTasksProvider(TasksProvider, TOMLProvider):
    def __init__(self, file_path: Path, task_adapter: InputTaskAdapter):
        super().__init__(file_path)
        self.task_adapter = task_adapter

    def get_tasks(self) -> list[Task]:
        raw_tasks = self._get_raw_data()
        input_tasks = InputTasks.model_validate(raw_tasks).root
        return self.task_adapter.get_domain_tasks(input_tasks)
