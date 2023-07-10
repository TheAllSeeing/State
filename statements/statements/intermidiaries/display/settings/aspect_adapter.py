from statements.domain.settings.aspect import Aspect
from statements.intermidiaries.display.color.adapter import ColorAdapter
from statements.intermidiaries.display.settings.aspect import DisplayAspect
from statements.intermidiaries.display.projects.project import DisplayProject


class AspectAdapter:
    def __init__(self, color_adapter: ColorAdapter):
        self.color_adapter = color_adapter

    def get_display_aspect(self, aspect: Aspect):
        color = self.color_adapter.get_display_color(aspect.name, aspect.color)

        return DisplayAspect(
            name=aspect.name,
            color=color,
            active_projects=[DisplayProject(name=project, color=color) for project in aspect.active_projects],
            passive_projects=[DisplayProject(name=project, color=color) for project in aspect.passive_projects],
            frozen_projects=[DisplayProject(name=project, color=color) for project in aspect.frozen_projects],
            archived_projects=[DisplayProject(name=project, color=color) for project in aspect.archived_projects],
        )
