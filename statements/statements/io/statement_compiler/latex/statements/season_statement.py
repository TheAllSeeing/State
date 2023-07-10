from pylatex import NewPage

from statements.intermidiaries.display.statements.season.statement import DisplaySeasonStatement
from statements.io.statement_compiler.latex.parts.season.conclusions import SeasonConclusions
from statements.io.statement_compiler.latex.parts.season.outline import SeasonOutline
from statements.io.statement_compiler.latex.parts.season.results import SeasonResults
from statements.io.statement_compiler.latex.parts.season.status import SeasonStatus
from statements.io.statement_compiler.latex.statements.base_statement import BaseStatement


class SeasonStatement(BaseStatement):
    def __init__(self, statement_model: DisplaySeasonStatement, **kwargs):
        super().__init__(statement_model, **kwargs)
        self.append(SeasonOutline(statement_model.outline))

        self.append(NewPage())
        self.append(SeasonStatus(statement_model.status))

        self.append(NewPage())
        self.append(SeasonResults(statement_model.results))

        self.append(NewPage())
        self.append(SeasonConclusions(statement_model.conclusions))
