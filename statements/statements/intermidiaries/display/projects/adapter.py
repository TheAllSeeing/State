from statements.domain.settings.aspect import Aspect
from statements.intermidiaries.display.color.adapter import ColorAdapter
from statements.intermidiaries.display.projects.project import DisplayProject

ProjectMap = dict[str, Aspect]


class ProjectAdapter:
    def __init__(self, color_adapter: ColorAdapter):
        self.color_adapter = color_adapter

    def get_display_project(self, project_name: str, projects_to_aspect: dict[str, Aspect]):
        aspect = projects_to_aspect[project_name]
        return DisplayProject(name=project_name, color=self.color_adapter.get_display_color(aspect.name, aspect.color))
