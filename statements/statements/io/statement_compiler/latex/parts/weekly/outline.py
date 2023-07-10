from statements.intermidiaries.display.parts.week.outline import DisplayWeekOutline
from statements.io.statement_compiler.latex.models.plan import Plan
from statements.io.statement_compiler.latex.parts import BasePart
from statements.io.statement_compiler.latex.sections.goals.statusless_goals import OutlineGoals
from statements.io.statement_compiler.latex.sections.habits.habits import Habits
from statements.io.statement_compiler.latex.sections.schedule import Schedule
from statements.io.statement_compiler.latex.sections.tasks.statusless_tasks import OutlineTasks
from statements.io.statement_compiler.latex.sections.vetoes.vetoes import Vetoes


class WeekOutline(BasePart):
    def __init__(self, outline_model: DisplayWeekOutline):
        super().__init__()
        self.append(Schedule(outline_model.schedule))
        self.append(OutlineGoals(outline_model.goals))
        self.append(Habits(outline_model.habits))
        self.append(Vetoes(outline_model.vetoes))
        self.append(OutlineTasks(outline_model.tasks))
        self.append(Plan(outline_model.plan))
