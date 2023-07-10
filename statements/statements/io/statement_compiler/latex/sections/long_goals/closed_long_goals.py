from pylatex import Itemize
from pylatex.base_classes import LatexObject

from statements.intermidiaries.display.long_goals.goal_closure import DisplayLongGoalClosure
from statements.io.statement_compiler.latex.models.long_goal_closure import LongGoalClosure
from statements.io.statement_compiler.latex.sections.base_section import BaseSection


class ClosedLongGoals(BaseSection):
    _title = 'Closed Goals'

    def __init__(self, goal_closures: list[DisplayLongGoalClosure]):
        self.goal_closures = goal_closures
        super().__init__()

    def make(self) -> LatexObject:
        goal_closure_list = Itemize()
        for goal_closure in self.goal_closures:
            goal_closure_list.add_item(LongGoalClosure(goal_closure))
        return goal_closure_list
