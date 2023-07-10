from pylatex.utils import bold

from statements.intermidiaries.display.issue.issue import DisplayIssue
from statements.io.statement_compiler.latex.utils.insight import Insight
from statements.io.statement_compiler.latex.utils.markdown import Markdown
from statements.io.statement_compiler.latex.wrappers import Emph
from statements.io.statement_compiler.latex.wrappers.group import Group
from statements.io.statement_compiler.latex.wrappers.new_paragraph import NewParagraph
from statements.io.statement_compiler.latex.wrappers.set_text_color import SetTextColor


class Issue(Group):
    def __init__(self, issue: DisplayIssue):
        super().__init__()
        self.append(SetTextColor(issue.project.color.name))
        self.append(Insight(issue.project, bold(issue.title), id_=issue.id_))
        self.append(NewParagraph())
        self.append(Markdown(issue.description))
        if issue.note:
            self.append(NewParagraph())
            self.append(Emph(Markdown(issue.note)))