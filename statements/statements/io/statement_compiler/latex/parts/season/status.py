from statements.intermidiaries.display.parts.season.status import DisplaySeasonStatus
from statements.io.statement_compiler.latex.parts import BasePart
from statements.io.statement_compiler.latex.sections.issues.issues import Issues
from statements.io.statement_compiler.latex.sections.long_goals.long_goals import LongGoals
from statements.io.statement_compiler.latex.sections.proposals import Proposals


class SeasonStatus(BasePart):
    def __init__(self, status_model: DisplaySeasonStatus):
        super().__init__()
        self.append(LongGoals(status_model.goals))
        self.append(Issues(status_model.issues))
        self.append(Proposals(status_model.open_proposals))
