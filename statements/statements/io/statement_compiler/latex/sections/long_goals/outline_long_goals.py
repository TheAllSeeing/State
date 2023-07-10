from pylatex import Itemize
from pylatex.base_classes import LatexObject

from statements.intermidiaries.display.long_goals.long_goal import DisplayLongGoal
from statements.io.statement_compiler.latex.models.long_goal import OutlineLongGoal
from statements.io.statement_compiler.latex.sections.base_section import BaseSection


class OutlineLongGoals(BaseSection):
    _title = 'Goals'

    def __init__(self, goals: list[DisplayLongGoal]):
        self.goals = goals
        super().__init__()

    def make(self) -> LatexObject:
        goals_list = Itemize()
        for goal in self.goals:
            goals_list.add_item(OutlineLongGoal(goal))
        return goals_list
