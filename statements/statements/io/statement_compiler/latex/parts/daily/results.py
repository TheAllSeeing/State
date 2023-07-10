from statements.intermidiaries.display.parts.day.results import DisplayDayResults
from statements.io.statement_compiler.latex.parts import BasePart
from statements.io.statement_compiler.latex.sections.day.diary import Diary
from statements.io.statement_compiler.latex.sections.day.rest import Rest
from statements.io.statement_compiler.latex.sections.day.sleep import Sleep
from statements.io.statement_compiler.latex.sections.incidents import Incidents
from statements.io.statement_compiler.latex.sections.issues.issue_results import IssueResults
from statements.io.statement_compiler.latex.sections.new_context import NewContext
from statements.io.statement_compiler.latex.sections.proposals import Proposals
from statements.io.statement_compiler.latex.sections.tasks.tasks import Tasks


class DayResults(BasePart):
    def __init__(self, results: DisplayDayResults):
        super().__init__()
        self.append(Incidents(results.incidents))
        self.append(NewContext(results.new_context))
        self.append(Tasks(results.resolved_tasks))
        self.append(Diary(results.diary))
        self.append(Sleep(results.sleep))
        self.append(Rest(results.rest))
        self.append(IssueResults(opened_issues=results.new_issues,
                                 closed_issues=results.closed_issues))
        self.append(Proposals(results.resolved_proposals))

