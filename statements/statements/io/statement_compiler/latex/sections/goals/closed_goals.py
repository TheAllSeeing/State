from pylatex import Itemize
from pylatex.base_classes import LatexObject

from statements.intermidiaries.display.goals.goal_closure import DisplayGoalClosure
from statements.io.statement_compiler.latex.models.goal_closure import GoalClosure
from statements.io.statement_compiler.latex.sections.base_section import BaseSection


class ClosedGoals(BaseSection):
    _title = 'Closed Goals'

    def __init__(self, goal_closures: list[DisplayGoalClosure]):
        self.goal_closures = goal_closures
        super().__init__()

    def make(self) -> LatexObject:
        goal_closure_list = Itemize()
        for goal_closure in self.goal_closures:
            goal_closure_list.add_item(GoalClosure(goal_closure))
        return goal_closure_list
