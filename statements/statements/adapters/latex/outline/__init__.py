from statements.adapters.latex.outline.long_goal import LongGoalAdapter
from statements.domain.outline.outline import Outline
from statements.io.latex.models.outline import LatexOutline


class OutlineAdapter:
    def __init__(self, goal_adapter: LongGoalAdapter):
        self.goal_adapter = goal_adapter

    def get_latex_outline(self, outline: Outline) -> LatexOutline:
        return LatexOutline(
            overview=outline.overview,
            schedule=[event.model_dump() for event in outline.schedule],
            goals=[self.goal_adapter.get_latex_goal(goal) for goal in outline.goals],
        )
