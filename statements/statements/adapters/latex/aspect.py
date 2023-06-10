from statements.adapters.latex.color import ColorAdapter
from statements.domain.settings.aspect import Aspect
from statements.io.latex.models.aspect import LatexAspect
from statements.io.latex.models.project import LatexProject


class AspectAdapter:
    def __init__(self, color_adapter: ColorAdapter):
        self.color_adapter = color_adapter

    def get_latex_aspect(self, aspect: Aspect):
        color = self.color_adapter.get_latex_color(aspect.name, aspect.color)

        return LatexAspect(
            name=aspect.name,
            color=color,
            active_projects=[LatexProject(name=project, color=color) for project in aspect.active_projects],
            passive_projects=[LatexProject(name=project, color=color) for project in aspect.passive_projects],
            frozen_projects=[LatexProject(name=project, color=color) for project in aspect.frozen_projects],
            archived_projects=[LatexProject(name=project, color=color) for project in aspect.archived_projects],
        )
