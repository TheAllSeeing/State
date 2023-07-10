from statements.domain.settings.aspect import Aspect
from statements.domain.project_status_change import ProjectStatusChange
from statements.domain.project_status_change import StatusChange
from statements.intermidiaries.display.projects.adapter import ProjectAdapter
from statements.intermidiaries.display.projects.project_status_change import DisplayProjectStatusChange, \
    DisplayStatusChange


class ProjectStatusChangeAdapter:
    def __init__(self, project_adapter: ProjectAdapter):
        self.project_adapter = project_adapter

    def get_display_status(self, status: StatusChange) -> DisplayStatusChange:
        return getattr(DisplayStatusChange, status.name)

    def get_display_status_changes(self, status_changes: list[ProjectStatusChange],
                                   projects_to_aspects: dict[str, Aspect]) -> dict[DisplayStatusChange,
    list[DisplayProjectStatusChange]]:
        results: dict[DisplayStatusChange, list[DisplayProjectStatusChange]] = {status_change: [] for status_change in
                                                                                DisplayStatusChange}
        for change in status_changes:
            display_status = self.get_display_status(change.status_change)
            results[display_status].append(
                DisplayProjectStatusChange(
                    project=self.project_adapter.get_display_project(change.project, projects_to_aspects),
                    project_stub=change.project_stub,
                    change_description=change.change_description
                )
            )
        return results
