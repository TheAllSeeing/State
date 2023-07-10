import os
from contextlib import contextmanager
from pathlib import Path
from typing import Generic, TypeVar

from statements.intermidiaries.display.statements.day.adapter import DailyStatementAdapter
from statements.intermidiaries.display.statements.month.adapter import MonthStatementAdapter
from statements.intermidiaries.display.statements.season.adapter import SeasonStatementAdapter
from statements.intermidiaries.display.statements.week.adapter import WeeklyStatementAdapter
from statements.io.statement_compiler.latex.statements.base_statement import BaseStatement
from statements.io.statement_compiler.latex.statements.daily_statement import DailyStatement
from statements.io.statement_compiler.latex.statements.monthly_statement import MonthlyStatement
from statements.io.statement_compiler.latex.statements.season_statement import SeasonStatement
from statements.io.statement_compiler.latex.statements.weekly_statement import WeeklyStatement
from statements.use_cases.ports.statement_compiler import StatementCompiler

PATH_VARIABLE_NAME = 'PATH'

TAdapter = TypeVar('TAdapter')


@contextmanager
def extended_path(path_addition: list[Path]):
    current_path = os.environ[PATH_VARIABLE_NAME]
    os.environ[PATH_VARIABLE_NAME] = ':'.join([current_path, *[str(path) for path in path_addition]])
    yield
    os.environ[PATH_VARIABLE_NAME] = current_path


class LatexCompiler(StatementCompiler, Generic[TAdapter]):
    _statement_class: type[BaseStatement] = None

    def __init__(self, statement_adapter: TAdapter, *, tinytex_bin: Path):
        self.statement_adapter = statement_adapter
        self.tinytex_bin = tinytex_bin

    def compile(self, statement: SeasonStatement, output_path: str, *, clean_tex: bool = True):
        statement = self._statement_class(self.statement_adapter.get_display_statement(statement))
        with extended_path([self.tinytex_bin]):
            statement.generate_pdf(output_path, clean_tex=clean_tex)


class SeasonLatexCompiler(LatexCompiler[SeasonStatementAdapter]):
    _statement_class = SeasonStatement


class MonthlyLatexCompiler(LatexCompiler[MonthStatementAdapter]):
    _statement_class = MonthlyStatement


class WeeklyLatexCompiler(LatexCompiler[WeeklyStatementAdapter]):
    _statement_class = WeeklyStatement


class DailyLatexCompiler(LatexCompiler[DailyStatementAdapter]):
    _statement_class = DailyStatement
