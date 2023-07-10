from pylatex import Document, NewPage

from statements.intermidiaries.display.statements.month.statement import DisplayMonthlyStatement
from statements.io.statement_compiler.latex.parts.monthly.conclusions import MonthConclusions
from statements.io.statement_compiler.latex.parts.monthly.outline import MonthOutline
from statements.io.statement_compiler.latex.parts.monthly.results import MonthResults
from statements.io.statement_compiler.latex.parts.monthly.status import MonthStatus
from statements.io.statement_compiler.latex.statements.base_statement import BaseStatement


class MonthlyStatement(BaseStatement):
    def __init__(self, statement_model: DisplayMonthlyStatement, **kwargs):
        super().__init__(statement_model, **kwargs)
        self.append(MonthOutline(statement_model.outline))

        self.append(NewPage())
        self.append(MonthStatus(statement_model.status))

        self.append(NewPage())
        self.append(MonthResults(statement_model.results))

        self.append(NewPage())
        self.append(MonthConclusions(statement_model.conclusions))
