from statements.intermidiaries.display.parts.day.outline import DisplayDayOutline
from statements.io.statement_compiler.latex.models.plan import Plan
from statements.io.statement_compiler.latex.parts import BasePart
from statements.io.statement_compiler.latex.sections.schedule import Schedule
from statements.io.statement_compiler.latex.sections.tasks.statusless_tasks import OutlineTasks
from statements.io.statement_compiler.latex.sections.vetoes.vetoes import Vetoes


class DayOutline(BasePart):
    def __init__(self, outline_model: DisplayDayOutline):
        super().__init__()
        self.append(Schedule(outline_model.schedule))
        self.append(Vetoes(outline_model.vetoes))
        self.append(OutlineTasks(outline_model.tasks))
        self.append(Plan(outline_model.plan))
