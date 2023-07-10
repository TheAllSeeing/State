from statements.intermidiaries.display.parts.month.outline import DisplayMonthOutline
from statements.io.statement_compiler.latex.models.plan import Plan
from statements.io.statement_compiler.latex.parts import BasePart
from statements.io.statement_compiler.latex.sections.goals.statusless_goals import OutlineGoals
from statements.io.statement_compiler.latex.sections.habits.habits import Habits
from statements.io.statement_compiler.latex.sections.schedule import Schedule
from statements.io.statement_compiler.latex.sections.vetoes.vetoes import Vetoes


class MonthOutline(BasePart):
    def __init__(self, outline_model: DisplayMonthOutline):
        super().__init__()
        self.append(Schedule(outline_model.schedule))
        self.append(OutlineGoals(outline_model.goals))
        self.append(Habits(outline_model.habits))
        self.append(Vetoes(outline_model.vetoes))
        self.append(Plan(outline_model.plan))
