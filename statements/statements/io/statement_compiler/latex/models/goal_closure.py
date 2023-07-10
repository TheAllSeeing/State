from pylatex.utils import italic

from statements.domain.validation_types import Markdown
from statements.intermidiaries.display.goals.goal_closure import DisplayGoalClosure
from statements.io.statement_compiler.latex.utils.markdown import Markdown
from statements.io.statement_compiler.latex.wrappers.break_ import Break
from statements.io.statement_compiler.latex.wrappers.group import Group
from statements.io.statement_compiler.latex.wrappers.new_paragraph import NewParagraph
from statements.io.statement_compiler.latex.wrappers.set_text_color import SetTextColor
from statements.io.statement_compiler.latex.wrappers.underline import Underline


class GoalClosure(Group):
    def __init__(self, goal_closure: DisplayGoalClosure):
        super().__init__()
        self.append(SetTextColor(goal_closure.goal.project.color.name))
        self.append(Underline(goal_closure.goal.id_))
        self.append(Markdown(goal_closure.goal.description))
        self.append(Break())
        self.append(italic(goal_closure.reason))
        self.append(NewParagraph())
