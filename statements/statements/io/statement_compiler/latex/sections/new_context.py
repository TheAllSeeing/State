from pylatex import Itemize
from pylatex.base_classes import LatexObject

from statements.intermidiaries.display.context.context import DisplayContextItem
from statements.io.statement_compiler.latex.models.context import ContextItem
from statements.io.statement_compiler.latex.sections.base_section import BaseSection


class NewContext(BaseSection):
    def __init__(self, contexts: list[DisplayContextItem]):
        self.contexts = contexts
        super().__init__()

    def make(self) -> LatexObject:
        context_list = Itemize()
        for context in self.contexts:
            context_list.add_item(ContextItem(context))
        return context_list
