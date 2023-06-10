from pylatex.base_classes import CommandBase


def __getattr__(attr: str) -> type[CommandBase]:
    return type(attr, (CommandBase,), {})
