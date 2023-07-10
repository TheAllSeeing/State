from abc import ABC

from statements.domain.incidents.incident import Incident
from statements.io.statement_providers.config_file.incidents.incident import IncidentsConfig
from statements.io.statement_providers.config_file.toml_provider import TOMLProvider


class IncidentsProvider(ABC):
    def get_incidents(self) -> list[Incident]:
        pass


class TOMLIncidentProvider(IncidentsProvider, TOMLProvider):
    def get_incidents(self) -> list[Incident]:
        raw_incidents = self._get_raw_data()
        incidents_config = IncidentsConfig.validate_python(raw_incidents)
        return [Incident(
            id_=incident.id_,
            project=project,
            title=incident.title,
            description=incident.description
        ) for project, project_incidents in incidents_config.items()
            for incident in project_incidents]
