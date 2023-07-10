from statements.intermidiaries.display.parts.week.conclusions import DisplayWeekConclusions
from statements.intermidiaries.display.parts.week.outline import DisplayWeekOutline
from statements.intermidiaries.display.parts.week.results import DisplayWeekResults
from statements.intermidiaries.display.parts.week.status import DisplayWeekStatus
from statements.intermidiaries.display.statements.base_statement import DisplayStatement


class DisplayWeeklyStatement(DisplayStatement):
    outline: DisplayWeekOutline
    status: DisplayWeekStatus
    results: DisplayWeekResults
    conclusions: DisplayWeekConclusions
