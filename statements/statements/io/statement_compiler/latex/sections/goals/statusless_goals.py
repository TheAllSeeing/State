from pylatex import Itemize
from pylatex.base_classes import LatexObject

from statements.intermidiaries.display.goals.goal import DisplayGoal
from statements.io.statement_compiler.latex.models.goal import OutlineGoal
from statements.io.statement_compiler.latex.sections.base_section import BaseSection


class StatuslessGoals(BaseSection):
    def __init__(self, goals: list[DisplayGoal]):
        self.goals = goals
        super().__init__()

    def make(self) -> LatexObject:
        goals_list = Itemize()
        for goal in self.goals:
            goals_list.add_item(OutlineGoal(goal))
        return goals_list


class OutlineGoals(StatuslessGoals):
    _title = 'Goals'


class NewGoals(StatuslessGoals):
    pass
