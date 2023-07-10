from pylatex import Itemize
from pylatex.base_classes import LatexObject

from statements.intermidiaries.display.long_goals.long_goal import DisplayLongGoal
from statements.io.statement_compiler.latex.models.long_goal import LongGoal
from statements.io.statement_compiler.latex.sections.base_section import BaseSection


class LongGoals(BaseSection):
    _title = 'Goals'
    def __init__(self, goals_statuses: list[DisplayLongGoal]):
        self.goal_statuses = goals_statuses
        super().__init__()

    def make(self) -> LatexObject:
        status_list = Itemize()
        for goal_status in self.goal_statuses:
            status_list.add_item(LongGoal(goal_status))
        return status_list


class NewLongGoals(LongGoals):
    _title = 'New Goals'
