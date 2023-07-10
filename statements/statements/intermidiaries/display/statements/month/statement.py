from statements.intermidiaries.display.parts.month.conclusions import DisplayMonthConclusions
from statements.intermidiaries.display.parts.month.outline import DisplayMonthOutline
from statements.intermidiaries.display.parts.month.results import DisplayMonthResults
from statements.intermidiaries.display.parts.month.status import DisplayMonthStatus
from statements.intermidiaries.display.statements.base_statement import DisplayStatement


class DisplayMonthlyStatement(DisplayStatement):
    outline: DisplayMonthOutline
    status: DisplayMonthStatus
    results: DisplayMonthResults
    conclusions: DisplayMonthConclusions
