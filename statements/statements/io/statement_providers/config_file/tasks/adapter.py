from statements.domain.tasks.task import Task
from statements.domain.validation_types import ID, ProjectName
from statements.io.statement_providers.config_file.tasks.task import InputTask
from statements.io.statement_providers.config_file.progress_status.adapter import InputProgressStatusAdapter


class InputTaskAdapter:
    def __init__(self, status_adapter: InputProgressStatusAdapter):
        self.status_adapter = status_adapter

    def get_domain_tasks(self, tasks: dict[ID, dict[ProjectName, InputTask]]) -> list[Task]:
        return [Task(id_=id_, project=project, description=task.description, note=task.note,
                     status=self.status_adapter.get_progress_status(task.status))
                for project, project_tasks in tasks.items()
                for id_, task in project_tasks.items()]
