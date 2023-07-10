import os
from pathlib import Path

from contextlib import contextmanager

from statements.use_cases.ports.statement_compiler import StatementCompiler
from statements.use_cases.ports.statement_provider import StatementProvider


@contextmanager
def cwd(directory: Path):
    current_dir = os.getcwd()
    os.chdir(directory)
    yield
    os.chdir(current_dir)


class StatementMaker:
    def __init__(self, provider: StatementProvider, compiler: StatementCompiler):
        self.provider = provider
        self.compiler = compiler

    def make(self, input_path: Path, output_path: Path, *, clean_tex: bool = None):
        if output_path.name.endswith('.pdf'):
            output_path = Path(str(output_path)[:-4])

        with cwd(input_path):
            self.compiler.compile(self.provider.get_statement(), output_path=output_path, clean_tex=clean_tex)
