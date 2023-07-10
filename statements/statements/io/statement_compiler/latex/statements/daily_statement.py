from pylatex import Document, NewPage

from statements.intermidiaries.display.statements.day.statement import DisplayDailyStatement
from statements.io.statement_compiler.latex.parts.daily.conclusions import DayConclusions
from statements.io.statement_compiler.latex.parts.daily.outline import DayOutline
from statements.io.statement_compiler.latex.parts.daily.results import DayResults
from statements.io.statement_compiler.latex.parts.daily.status import DayStatus
from statements.io.statement_compiler.latex.statements.base_statement import BaseStatement


class DailyStatement(BaseStatement):
    def __init__(self, statement_model: DisplayDailyStatement, **kwargs):
        super().__init__(statement_model, **kwargs)
        self.append(DayOutline(statement_model.outline))

        self.append(NewPage())
        self.append(DayStatus(statement_model.status))

        self.append(NewPage())
        self.append(DayResults(statement_model.results))

        self.append(NewPage())
        self.append(DayConclusions(statement_model.conclusions))
