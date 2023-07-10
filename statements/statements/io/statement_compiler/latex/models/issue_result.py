from pylatex.utils import italic

from statements.intermidiaries.display.issue.issue import DisplayIssue
from statements.io.statement_compiler.latex.wrappers.break_ import Break
from statements.io.statement_compiler.latex.wrappers.group import Group
from statements.io.statement_compiler.latex.wrappers.set_text_color import SetTextColor
from statements.io.statement_compiler.latex.utils.insight import Insight


class IssueResult(Group):
    def __init__(self, issue: DisplayIssue):
        super().__init__()
        self.append(SetTextColor(issue.project.color.name))
        self.append(Insight(issue.project, issue.title, id_=issue.id_))
        if issue.note:
            self.append(Break())
            self.append(italic(issue.note))
