from pylatex import NoEscape, Command
from pylatex.base_classes import LatexObject


class Skip(LatexObject):
    def __init__(self, count: int):
        super().__init__()
        self.count = count

    def dumps(self) -> str:
        return Command('vspace', NoEscape(f'{self.count}\\baselineskip')).dumps()