from statements.intermidiaries.display.parts.month.status import DisplayMonthStatus
from statements.io.statement_compiler.latex.parts import BasePart
from statements.io.statement_compiler.latex.sections.goals.goals import Goals
from statements.io.statement_compiler.latex.sections.issues.issues import Issues
from statements.io.statement_compiler.latex.sections.proposals import Proposals


class MonthStatus(BasePart):
    def __init__(self, status_model: DisplayMonthStatus):
        super().__init__()
        self.append(Goals(status_model.goals))
        self.append(Issues(status_model.issues))
        self.append(Proposals(status_model.open_proposals))
