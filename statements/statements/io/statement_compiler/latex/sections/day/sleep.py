from pylatex import Tabular, NoEscape
from pylatex.base_classes import LatexObject

from statements.intermidiaries.display.day.day import DisplaySleep
from statements.io.statement_compiler.latex.sections.base_section import BaseSection
from statements.io.statement_compiler.latex.wrappers import TextBF as Bold


class Sleep(BaseSection):
    def __init__(self, sleep: DisplaySleep):
        self.sleep = sleep
        super().__init__()

    def make(self) -> LatexObject:
        table = Tabular('r l')
        for key, item in self.sleep:
            table.add_row([Bold(key.title()), item])
        return table
