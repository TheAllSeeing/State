from pylatex.utils import italic

from statements.intermidiaries.display.tasks.task import DisplayTask
from statements.io.statement_compiler.latex.models.progress_symbol import ProgressSymbol
from statements.io.statement_compiler.latex.utils.insight import Insight
from statements.io.statement_compiler.latex.utils.markdown import Markdown
from statements.io.statement_compiler.latex.wrappers.break_ import Break
from statements.io.statement_compiler.latex.wrappers.group import Group
from statements.io.statement_compiler.latex.wrappers.new_paragraph import NewParagraph
from statements.io.statement_compiler.latex.wrappers.set_text_color import SetTextColor
from statements.io.statement_compiler.latex.wrappers.underline import Underline


class OutlineTask(Insight):
    def __init__(self, task_model: DisplayTask):
        super().__init__(task_model.project, Markdown(task_model.description), id_=task_model.id_)


class Task(Group):
    def __init__(self, task: DisplayTask):
        super().__init__()
        self.append(SetTextColor(task.project.color.name))
        self.append(Underline(task.id_))
        self.append(Markdown(task.description))
        self.append(ProgressSymbol(task.status))
        if task.note:
            self.append(Break())
            self.append(italic(task.note))
            self.append(NewParagraph())
