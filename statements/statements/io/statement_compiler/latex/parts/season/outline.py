from statements.intermidiaries.display.parts.season.outline import DisplaySeasonOutline
from statements.io.statement_compiler.latex.models.plan import Plan
from statements.io.statement_compiler.latex.parts import BasePart
from statements.io.statement_compiler.latex.sections.habits.habits import Habits
from statements.io.statement_compiler.latex.sections.long_goals.outline_long_goals import OutlineLongGoals
from statements.io.statement_compiler.latex.sections.schedule import Schedule
from statements.io.statement_compiler.latex.sections.vetoes.vetoes import Vetoes
from statements.io.statement_compiler.latex.utils.markdown import Markdown


class SeasonOutline(BasePart):
    def __init__(self, outline_model: DisplaySeasonOutline):
        super().__init__()
        self.append(Markdown(outline_model.overview))
        self.append(Schedule(outline_model.schedule))
        self.append(OutlineLongGoals(outline_model.goals))
        self.append(Habits(outline_model.habits))
        self.append(Vetoes(outline_model.vetoes))
        self.append(Plan(outline_model.plan))
