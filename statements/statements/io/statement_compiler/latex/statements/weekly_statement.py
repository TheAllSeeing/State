from pylatex import Document, NewPage

from statements.intermidiaries.display.statements.week.statement import DisplayWeeklyStatement
from statements.io.statement_compiler.latex.parts.weekly.conclusions import WeekConclusions
from statements.io.statement_compiler.latex.parts.weekly.outline import WeekOutline
from statements.io.statement_compiler.latex.parts.weekly.results import WeekResults
from statements.io.statement_compiler.latex.parts.weekly.status import WeekStatus
from statements.io.statement_compiler.latex.statements.base_statement import BaseStatement


class WeeklyStatement(BaseStatement):
    def __init__(self, statement_model: DisplayWeeklyStatement, **kwargs):
        super().__init__(statement_model, **kwargs)
        self.append(WeekOutline(statement_model.outline))

        self.append(NewPage())
        self.append(WeekStatus(statement_model.status))

        self.append(NewPage())
        self.append(WeekResults(statement_model.results))

        self.append(NewPage())
        self.append(WeekConclusions(statement_model.conclusions))
