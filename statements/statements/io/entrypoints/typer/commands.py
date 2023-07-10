from pathlib import Path

import typer
from pylatex.errors import CompilerError
from rich import print
from typer import Argument, Option
from typing_extensions import Annotated
from watchfiles import watch as watch_files, Change

from statements.domain.settings.scope import StatementType
from statements.io.entrypoints.typer.doc_generator import FormattedDocFunction, IDocFormatter
from statements.use_cases.statement_maker import StatementMaker

InputPath = Annotated[Path, Argument(exists=True, dir_okay=True, file_okay=False, readable=True)]
OutputPath = Annotated[Path, Option(file_okay=True, dir_okay=False)]


class MakerCommands(IDocFormatter):
    def __init__(self, statement_maker: StatementMaker, type_: StatementType):
        self.type_ = type_
        self.maker = statement_maker
        self.default_name = Path(self.type_.value.title())

    @FormattedDocFunction
    def make(self, base_dir: InputPath = '.', *, output_path: OutputPath = None,
             clean_tex: bool = True, watch: bool = False):
        """
        Generates a {statement_type} statement PDF from input TOML files.

        Args:
            base_dir: The directory containing statement input files
            output_path: the path to generate the PDF into
            clean_tex: whether to clean up tex files after generating.
            watch: whether to watch files for changes instead of compiling once
        """

        output_path = output_path or self.default_name

        if watch:
            print(f'[green]Watching {base_dir}, will compile into [bold]{self.type_.value.title()} Statement[/bold] '
                  f'at {output_path} on change...[/green]')
            for changes in watch_files(base_dir, watch_filter=self.__is_source_change_event):
                try:
                    self.maker.make(input_path=base_dir, output_path=output_path, clean_tex=clean_tex)
                except FileNotFoundError as e:
                    print(f'[yellow]Failed to compile: {e.filename} not found[/yellow]')
                except Exception as e:
                    print(f'[yellow]Compilation failed: {e}[/yellow]')
                else:
                    print(
                        f'[green]'
                        f'Recompiled {output_path} ('
                        f'{", ".join(["[magenta]" + file_ + "[/magenta]" for change, file_ in changes])} modified)'
                        f'[/green]')
        else:
            try:
                self.maker.make(input_path=base_dir, output_path=output_path, clean_tex=clean_tex)
            except FileNotFoundError as e:
                print(f'[yellow]Failed to compile: {e.filename} not found[/yellow]')
            except Exception as e:
                print(f'[yellow]Compilation failed: {e}[/yellow]')
            else:
                if not str(output_path).endswith('.pdf'):
                    output_path = str(output_path) + '.pdf'
                print(f'[green]Compiled [italic]{base_dir}[/italic] into [bold]{output_path}[/bold][/green]')
                typer.launch(str(output_path))

    def get_formatting_dict(self) -> dict[str, str]:
        return {'statement_type': self.type_.value}

    def __is_source_change_event(self, change: Change, path: str):
        return change is Change.modified and path.endswith(('.toml', '.md'))
