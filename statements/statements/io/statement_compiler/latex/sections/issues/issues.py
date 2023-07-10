from pylatex import Itemize
from pylatex.base_classes import LatexObject

from statements.intermidiaries.display.issue.issue import DisplayIssue
from statements.io.statement_compiler.latex.models.issue import Issue
from statements.io.statement_compiler.latex.sections.base_section import BaseSection


class Issues(BaseSection):
    def __init__(self, issues: list[DisplayIssue]):
        self.issues = issues
        super().__init__()

    def make(self) -> LatexObject:
        issue_list = Itemize()
        for issue in self.issues:
            issue_list.add_item(Issue(issue))
        return issue_list
