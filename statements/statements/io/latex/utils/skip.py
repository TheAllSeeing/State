from pylatex.base_classes import LatexObject
from pylatex import NoEscape, Command

class Skip(LatexObject):
    def __init__(self, count: int):
        self.count = count

    def dumps(self) -> str:
        return Command('vspace', NoEscape(f'{self.count}\\baselineskip')).dumps()