from pylatex.utils import italic

from statements.io.latex.latex_objects.markdown import Markdown
from statements.io.latex.models.long_goal import LatexLongGoal
from statements.io.latex.utils.group import Group
from statements.io.latex.utils.set_text_color import SetTextColor
from statements.io.latex.utils.underline import Underline


class LongGoal(Group):
    def __init__(self, goal_model: LatexLongGoal):
        super().__init__()
        self.append(SetTextColor(goal_model.color.name))
        self.append(Underline(goal_model.id_))
        self.append(Markdown(goal_model.description))
        self.append(f'---')
        self.append(italic(goal_model.projects))


