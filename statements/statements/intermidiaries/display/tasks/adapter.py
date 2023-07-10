from statements.domain.tasks.task import Task
from statements.domain.settings.aspect import Aspect
from statements.intermidiaries.display.tasks.task import DisplayTask
from statements.intermidiaries.display.progress_status.adapter import ProgressStatusAdapter
from statements.intermidiaries.display.projects.adapter import ProjectAdapter


class TaskAdapter:
    def __init__(self, project_adapter: ProjectAdapter, progress_status_adapter: ProgressStatusAdapter):
        self.project_adapter = project_adapter
        self.status_adapter = progress_status_adapter

    def get_display_task(self, task: Task, projects_to_aspects: dict[str, Aspect]) -> DisplayTask:
        return DisplayTask(
            id_=task.id_,
            project=self.project_adapter.get_display_project(task.project, projects_to_aspects),
            description=task.description,
            status=self.status_adapter.get_progress_status(task.status),
            note=task.note
        )
