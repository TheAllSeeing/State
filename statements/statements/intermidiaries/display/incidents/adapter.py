from statements.domain.settings.aspect import Aspect
from statements.domain.incidents.incident import Incident
from statements.intermidiaries.display.projects.adapter import ProjectAdapter
from statements.intermidiaries.display.incidents.incident import DisplayIncident


class IncidentAdapter:
    def __init__(self, project_adapter: ProjectAdapter):
        self.project_adapter = project_adapter

    def get_display_incident(self, incident: Incident, projects_to_aspects: dict[str, Aspect]):
        return DisplayIncident(
            id_=incident.id_,
            project=self.project_adapter.get_display_project(incident.project, projects_to_aspects),
            title=incident.title,
            description=incident.description
        )
