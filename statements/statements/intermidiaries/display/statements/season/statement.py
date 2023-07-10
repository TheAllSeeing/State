from statements.intermidiaries.display.parts.season.conclusions import DisplaySeasonConclusions
from statements.intermidiaries.display.parts.season.outline import DisplaySeasonOutline
from statements.intermidiaries.display.parts.season.results import DisplaySeasonResults
from statements.intermidiaries.display.parts.season.status import DisplaySeasonStatus
from statements.intermidiaries.display.statements.base_statement import DisplayStatement


class DisplaySeasonStatement(DisplayStatement):
    outline: DisplaySeasonOutline
    status: DisplaySeasonStatus
    results: DisplaySeasonResults
    conclusions: DisplaySeasonConclusions
