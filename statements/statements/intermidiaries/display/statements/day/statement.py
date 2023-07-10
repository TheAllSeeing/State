from statements.intermidiaries.display.parts.day.conclusions import DisplayDayConclusions
from statements.intermidiaries.display.parts.day.outline import DisplayDayOutline
from statements.intermidiaries.display.parts.day.results import DisplayDayResults
from statements.intermidiaries.display.parts.day.status import DisplayDayStatus
from statements.intermidiaries.display.statements.base_statement import DisplayStatement


class DisplayDailyStatement(DisplayStatement):
    outline: DisplayDayOutline
    status: DisplayDayStatus
    results: DisplayDayResults
    conclusions: DisplayDayConclusions
