from statements.intermidiaries.display.parts.season.results import DisplaySeasonResults
from statements.io.statement_compiler.latex.parts import BasePart
from statements.io.statement_compiler.latex.sections.incidents import Incidents
from statements.io.statement_compiler.latex.sections.issues.issue_results import IssueResults
from statements.io.statement_compiler.latex.sections.long_goals.long_goals import LongGoals
from statements.io.statement_compiler.latex.sections.new_context import NewContext
from statements.io.statement_compiler.latex.sections.proposals import Proposals
from statements.io.statement_compiler.latex.sections.vetoes.veto_maintenance import VetoMaintenance


class SeasonResults(BasePart):
    def __init__(self, results: DisplaySeasonResults):
        super().__init__()
        self.append(Incidents(results.incidents))
        self.append(NewContext(results.new_context))
        self.append(VetoMaintenance(results.veto_maintenance))
        self.append(LongGoals(results.resolved_goals))
        self.append(IssueResults(opened_issues=results.new_issues,
                                 closed_issues=results.closed_issues))
        self.append(Proposals(results.resolved_proposals))

