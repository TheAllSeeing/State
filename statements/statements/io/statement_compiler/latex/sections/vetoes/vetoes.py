from pylatex import Itemize
from pylatex.base_classes import LatexObject

from statements.intermidiaries.display.vetoes.veto import DisplayVeto
from statements.io.statement_compiler.latex.models.veto import Veto
from statements.io.statement_compiler.latex.sections.base_section import BaseSection


class Vetoes(BaseSection):
    def __init__(self, vetoes: list[DisplayVeto]):
        self.vetoes = vetoes
        super().__init__()

    def make(self) -> LatexObject:
        veto_list = Itemize()
        for veto in self.vetoes:
            veto_list.add_item(Veto(veto))
        return veto_list
