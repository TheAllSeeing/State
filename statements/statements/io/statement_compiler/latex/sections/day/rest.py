from pylatex import Itemize
from pylatex.base_classes import LatexObject

from statements.intermidiaries.display.day.day import DisplayRest
from statements.io.statement_compiler.latex.models.rest_item import RestItem
from statements.io.statement_compiler.latex.sections.base_section import BaseSection


class Rest(BaseSection):
    def __init__(self, items: DisplayRest):
        self.items = items.root
        super().__init__()

    def make(self) -> LatexObject:
        items = Itemize()
        for item in self.items:
            items.add_item(RestItem(item))
        return items
