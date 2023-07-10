from statements.intermidiaries.display.parts.week.status import DisplayWeekStatus
from statements.io.statement_compiler.latex.parts import BasePart
from statements.io.statement_compiler.latex.sections.goals.goals import Goals
from statements.io.statement_compiler.latex.sections.issues.issues import Issues
from statements.io.statement_compiler.latex.sections.proposals import Proposals
from statements.io.statement_compiler.latex.sections.tasks.tasks import Tasks


class WeekStatus(BasePart):
    def __init__(self, status_model: DisplayWeekStatus):
        super().__init__()
        self.append(Goals(status_model.goals))
        self.append(Tasks(status_model.open_tasks))
        self.append(Issues(status_model.issues))
        self.append(Proposals(status_model.open_proposals))
