from pylatex import NoEscape
from pylatex.utils import italic

from statements.intermidiaries.display.goals.goal import DisplayGoal
from statements.io.statement_compiler.latex.utils.insight import Insight
from statements.io.statement_compiler.latex.wrappers.break_ import Break
from statements.io.statement_compiler.latex.wrappers.group import Group
from statements.io.statement_compiler.latex.wrappers.new_paragraph import NewParagraph
from statements.io.statement_compiler.latex.wrappers.set_text_color import SetTextColor
from statements.io.statement_compiler.latex.wrappers.underline import Underline
from statements.io.statement_compiler.latex.models.progress_symbol import ProgressSymbol
from statements.io.statement_compiler.latex.utils.markdown import Markdown


class OutlineGoal(Insight):
    def __init__(self, goal_model: DisplayGoal):
        super().__init__(goal_model.project, Markdown(goal_model.description), id_=goal_model.id_)


class Goal(Group):
    def __init__(self, goal: DisplayGoal):
        super().__init__()
        self.append(SetTextColor(goal.project.color.name))
        self.append(Underline(goal.id_))
        self.append(Markdown(goal.description))
        self.append(ProgressSymbol(goal.status))
        if goal.note:
            self.append(Break())
            self.append(italic(goal.note))
            self.append(NewParagraph())
