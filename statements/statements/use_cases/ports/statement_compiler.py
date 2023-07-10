from abc import ABC

from statements.domain.statements.base_statement import Statement


class StatementCompiler(ABC):

    def compile(self, statement: Statement, output_path: str):
        pass
