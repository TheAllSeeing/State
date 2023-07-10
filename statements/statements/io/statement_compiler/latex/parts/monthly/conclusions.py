from statements.intermidiaries.display.parts.month.conclusions import DisplayMonthConclusions
from statements.io.statement_compiler.latex.parts import BasePart
from statements.io.statement_compiler.latex.sections.goals.closed_goals import ClosedGoals
from statements.io.statement_compiler.latex.sections.goals.statusless_goals import NewGoals
from statements.io.statement_compiler.latex.sections.notes import Notes
from statements.io.statement_compiler.latex.sections.proposals import Proposals


class MonthConclusions(BasePart):
    def __init__(self, conclusions: DisplayMonthConclusions):
        super().__init__()
        self.append(NewGoals(conclusions.new_goals))
        self.append(ClosedGoals(conclusions.closed_goals))
        self.append(Proposals(conclusions.new_proposals))
        self.append(Notes(conclusions.notes))
