from statements.intermidiaries.display.parts.month.results import DisplayMonthResults
from statements.io.statement_compiler.latex.parts import BasePart
from statements.io.statement_compiler.latex.sections.goals.goals import Goals
from statements.io.statement_compiler.latex.sections.habits.habit_maintenance import HabitMaintenance
from statements.io.statement_compiler.latex.sections.incidents import Incidents
from statements.io.statement_compiler.latex.sections.issues.issue_results import IssueResults
from statements.io.statement_compiler.latex.sections.new_context import NewContext
from statements.io.statement_compiler.latex.sections.proposals import Proposals
from statements.io.statement_compiler.latex.sections.vetoes.veto_maintenance import VetoMaintenance


class MonthResults(BasePart):
    def __init__(self, results: DisplayMonthResults):
        super().__init__()
        self.append(Incidents(results.incidents))
        self.append(NewContext(results.new_context))
        self.append(HabitMaintenance(results.habit_maintenance))
        self.append(VetoMaintenance(results.veto_maintenance))
        self.append(Goals(results.resolved_goals))
        self.append(IssueResults(opened_issues=results.new_issues,
                                 closed_issues=results.closed_issues))
        self.append(Proposals(results.resolved_proposals))

