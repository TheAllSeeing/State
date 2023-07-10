from abc import abstractmethod, ABC

from statements.domain.project_status_change import ProjectStatusChange
from statements.domain.project_status_change import StatusChange
from statements.io.statement_providers.config_file.project_changes.project_changes import ProjectStatusChangesConfig
from statements.io.statement_providers.config_file.toml_provider import TOMLProvider


class ProjectStatusChangeProvider(ABC):
    @abstractmethod
    def get_status_changes(self) -> list[ProjectStatusChange]:
        pass


class TOMLProjectStatusChangeProvider(ProjectStatusChangeProvider, TOMLProvider):
    def get_status_changes(self) -> list[ProjectStatusChange]:
        raw_changes = self._get_raw_data()
        input_changes = ProjectStatusChangesConfig.model_validate(raw_changes)
        return [
            ProjectStatusChange(project=project, status_change=StatusChange(status.lower()),
                                project_stub=change.project_stub, change_description=change.change_description)
            for status, project_changes in input_changes
            for project, change in project_changes.items()
        ]
