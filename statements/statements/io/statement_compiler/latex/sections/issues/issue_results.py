from pylatex import Itemize
from pylatex.base_classes import LatexObject
from pylatex.base_classes.containers import Fragment
from pylatex.section import Paragraph

from statements.intermidiaries.display.issue.issue import DisplayIssue
from statements.io.statement_compiler.latex.models.issue_result import IssueResult
from statements.io.statement_compiler.latex.sections.base_section import BaseSection


class IssueResults(BaseSection):
    _title = 'Issues'

    def __init__(self, opened_issues: list[DisplayIssue], closed_issues: list[DisplayIssue]):
        self.opened_issues = opened_issues
        self.closed_issues = closed_issues
        super().__init__()

    def make(self) -> LatexObject:
        fragment = Fragment()

        if self.opened_issues:
            with fragment.create(Paragraph('New:')) as new_subsection:
                with new_subsection.create(Itemize()) as new_issue_list:
                    for issue in self.opened_issues:
                        new_issue_list.add_item(IssueResult(issue))

        if self.closed_issues:
            with fragment.create(Paragraph('Closed:')) as new_subsection:
                with new_subsection.create(Itemize()) as new_issue_list:
                    for issue in self.closed_issues:
                        new_issue_list.add_item(IssueResult(issue))

        return fragment

