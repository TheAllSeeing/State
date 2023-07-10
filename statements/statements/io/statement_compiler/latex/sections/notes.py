from pylatex.base_classes import LatexObject

from statements.domain.validation_types import Markdown as MarkdownString
from statements.io.statement_compiler.latex.sections.base_section import BaseSection
from statements.io.statement_compiler.latex.utils.markdown import Markdown


class Notes(BaseSection):
    def __init__(self, notes: MarkdownString):
        self.notes = notes
        super().__init__()

    def make(self) -> LatexObject:
        return Markdown(self.notes)
