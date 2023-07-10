from pylatex import Command, NoEscape

class Define(Command):
    def __init__(self, command_name, *args, **kwargs):
        super().__init__(NoEscape(r'\def\\' + command_name), *args, **kwargs)