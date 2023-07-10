from statements.domain.settings.aspect import Aspect
from statements.domain.vetoes.veto import Veto
from statements.intermidiaries.display.projects.adapter import ProjectAdapter
from statements.intermidiaries.display.vetoes.veto import DisplayVeto


class VetoAdapter:
    def __init__(self, project_adapter: ProjectAdapter):
        self.project_adapter = project_adapter

    def get_display_veto(self, veto: Veto, projects_to_aspects: dict[str, Aspect]) -> DisplayVeto:
        return DisplayVeto(
            project=self.project_adapter.get_display_project(veto.project, projects_to_aspects),
            description=veto.description
        )