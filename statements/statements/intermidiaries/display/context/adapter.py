from statements.domain.settings.aspect import Aspect
from statements.domain.incidents.context import ContextItem
from statements.intermidiaries.display.projects.adapter import ProjectAdapter
from statements.intermidiaries.display.context.context import DisplayContextItem


class ContextAdapter:
    def __init__(self, project_adapter: ProjectAdapter):
        self.project_adapter = project_adapter

    def get_display_context(self, context_item: ContextItem, projects_to_aspects: dict[str, Aspect]) -> DisplayContextItem:
        return DisplayContextItem(
            project=self.project_adapter.get_display_project(context_item.project, projects_to_aspects),
            description=context_item.description
        )
