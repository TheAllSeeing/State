from pylatex import NoEscape
from pylatex.utils import italic

from statements.intermidiaries.display.long_goals.long_goal import DisplayLongGoal
from statements.io.statement_compiler.latex.wrappers.break_ import Break
from statements.io.statement_compiler.latex.wrappers.group import Group
from statements.io.statement_compiler.latex.wrappers.new_paragraph import NewParagraph
from statements.io.statement_compiler.latex.wrappers.set_text_color import SetTextColor
from statements.io.statement_compiler.latex.wrappers.underline import Underline
from statements.io.statement_compiler.latex.models.progress_symbol import ProgressSymbol
from statements.io.statement_compiler.latex.utils.markdown import Markdown


class OutlineLongGoal(Group):
    def __init__(self, goal_model: DisplayLongGoal):
        super().__init__()
        self.append(SetTextColor(goal_model.color.name))
        self.append(Underline(goal_model.id_))
        self.append(Markdown(goal_model.description))
        self.append(NoEscape('---'))
        self.append(italic(goal_model.projects))


class LongGoal(Group):
    def __init__(self, goal: DisplayLongGoal):
        super().__init__()
        self.append(SetTextColor(goal.color.name))
        self.append(Underline(goal.id_))
        self.append(Markdown(goal.description))
        self.append(ProgressSymbol(goal.status))
        if goal.note:
            self.append(Break())
            self.append(italic(goal.note))
            self.append(NewParagraph())
