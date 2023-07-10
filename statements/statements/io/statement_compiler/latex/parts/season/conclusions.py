from statements.intermidiaries.display.parts.season.conclusions import DisplaySeasonConclusions
from statements.io.statement_compiler.latex.parts import BasePart
from statements.io.statement_compiler.latex.sections.long_goals.closed_long_goals import ClosedLongGoals
from statements.io.statement_compiler.latex.sections.long_goals.long_goals import NewLongGoals
from statements.io.statement_compiler.latex.sections.notes import Notes
from statements.io.statement_compiler.latex.sections.project_status_changes import ProjectStatusChanges
from statements.io.statement_compiler.latex.sections.proposals import Proposals


class SeasonConclusions(BasePart):
    def __init__(self, conclusions: DisplaySeasonConclusions):
        super().__init__()
        self.append(ProjectStatusChanges(conclusions.project_status_changes))
        self.append(NewLongGoals(conclusions.new_goals))
        self.append(ClosedLongGoals(conclusions.closed_goals))
        self.append(Proposals(conclusions.new_proposals))
        self.append(Notes(conclusions.notes))
