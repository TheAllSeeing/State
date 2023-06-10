from statements.adapters.latex.color import ColorAdapter
from statements.domain.outline.long_goal import LongGoal
from statements.domain.settings.aspect import Aspect
from statements.io.latex.models.long_goal import LatexLongGoal


class LongGoalAdapter:
    def __init__(self, color_adapter: ColorAdapter, projects: dict[str, Aspect]):
        self.color_adapter = color_adapter
        self.projects_to_aspects = projects

    def get_latex_goal(self, goal: LongGoal) -> LatexLongGoal:
        aspect = self.projects_to_aspects[goal.projects[0]]
        return LatexLongGoal(
            id_=goal.id_,
            color=self.color_adapter.get_latex_color(aspect.name, aspect.color),
            projects=', '.join(goal.projects),
            description=goal.description,
        )
