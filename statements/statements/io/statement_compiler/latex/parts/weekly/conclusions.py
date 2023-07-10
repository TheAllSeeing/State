from statements.intermidiaries.display.parts.week.conclusions import DisplayWeekConclusions
from statements.io.statement_compiler.latex.parts import BasePart
from statements.io.statement_compiler.latex.sections.goals.statusless_goals import NewGoals
from statements.io.statement_compiler.latex.sections.notes import Notes
from statements.io.statement_compiler.latex.sections.proposals import Proposals
from statements.io.statement_compiler.latex.sections.tasks.statusless_tasks import NewTasks


class WeekConclusions(BasePart):
    def __init__(self, conclusions: DisplayWeekConclusions):
        super().__init__()
        self.append(NewGoals(conclusions.new_goals))
        self.append(NewTasks(conclusions.new_tasks))
        self.append(Proposals(conclusions.new_proposals))
        self.append(Notes(conclusions.notes))
