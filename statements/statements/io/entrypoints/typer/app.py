import inspect
from inspect import Parameter
from types import MethodType
from typing import Callable, Annotated

import docstring_parser.google
from typer import Typer, Option, Argument
from typer.models import CommandFunctionType, OptionInfo, ArgumentInfo

from statements.io.entrypoints.typer.commands import MakerCommands


class StateCLI(Typer):
    def __init__(self, season_commands: MakerCommands, month_commands: MakerCommands,
                 week_commands: MakerCommands, day_commands: MakerCommands, **kwargs):
        super().__init__(**kwargs)
        self.command('season')(season_commands.make)
        self.command('month')(month_commands.make)
        self.command('week')(week_commands.make)
        self.command('day')(day_commands.make)

    def command(self, *args, **kwargs) -> Callable[[CommandFunctionType], CommandFunctionType]:
        command_registerer = super().command(*args, **kwargs)

        def decorate_with_docstring_processing(func: CommandFunctionType) -> CommandFunctionType:
            actual_func = func.__func__ if isinstance(func, MethodType) else func
            func_docstring = docstring_parser.google.parse(actual_func.__doc__)
            func_signature = inspect.signature(actual_func)

            for i, (_, parameter) in enumerate(func_signature.parameters.items()):
                if isinstance(func, MethodType) and i == 0:  # Bound parameter
                    continue

                docstring = [param for param in func_docstring.params if param.arg_name == parameter.name]
                if not docstring:
                    raise ValueError('Every argument in a typer command must have docstring')
                docstring = docstring[0].description

                if isinstance(parameter.default, (OptionInfo, ArgumentInfo)):
                    if not parameter.default.help:
                        parameter.default.help = docstring

                elif hasattr(parameter.annotation, '__metadata__'):
                    annotations = parameter.annotation.__metadata__
                    for i, data in enumerate(annotations):
                        if isinstance(data, (OptionInfo, ArgumentInfo)):
                            if not data.help:
                                parameter.annotation.__metadata__[i].help = docstring
                else:
                    if parameter.kind == Parameter.KEYWORD_ONLY or parameter.kind == Parameter.VAR_KEYWORD:
                        arg_kind = Option
                    else:
                        arg_kind = Argument

                    parameter._annotation = Annotated[
                        parameter.annotation, arg_kind(help=docstring)
                    ]

            description = ''
            if func_docstring.short_description:
                description += func_docstring.short_description
            if func_docstring.long_description:
                if description:
                    description += '\n\n'
                description += func_docstring.long_description

            def result(*args, **kwargs):
                return actual_func(*args, **kwargs)

            result.__signature__ = func_signature
            result.__doc__ = description

            if isinstance(func, MethodType):
                result = MethodType(result, func.__self__)

            return command_registerer(result)

        return decorate_with_docstring_processing
