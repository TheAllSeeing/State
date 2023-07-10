from statements.intermidiaries.display.parts.day.conclusions import DisplayDayConclusions
from statements.io.statement_compiler.latex.parts import BasePart
from statements.io.statement_compiler.latex.sections.notes import Notes
from statements.io.statement_compiler.latex.sections.proposals import Proposals
from statements.io.statement_compiler.latex.sections.tasks.statusless_tasks import NewTasks


class DayConclusions(BasePart):
    def __init__(self, conclusions: DisplayDayConclusions):
        super().__init__()
        self.append(NewTasks(conclusions.new_tasks))
        self.append(Proposals(conclusions.new_proposals))
        self.append(Notes(conclusions.notes))
