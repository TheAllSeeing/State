from pylatex import Itemize
from pylatex.base_classes import LatexObject

from statements.intermidiaries.display.goals.goal import DisplayGoal
from statements.io.statement_compiler.latex.models.goal import Goal
from statements.io.statement_compiler.latex.sections.base_section import BaseSection


class Goals(BaseSection):
    def __init__(self, goals_statuses: list[DisplayGoal]):
        self.goal_statuses = goals_statuses
        super().__init__()

    def make(self) -> LatexObject:
        status_list = Itemize()
        for goal_status in self.goal_statuses:
            status_list.add_item(Goal(goal_status))
        return status_list
