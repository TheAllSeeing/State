from pylatex import Itemize
from pylatex.base_classes import LatexObject

from statements.intermidiaries.display.day.day import DisplayDiary
from statements.io.statement_compiler.latex.sections.base_section import BaseSection
from statements.io.statement_compiler.latex.wrappers import Item, TextBF as Bold


class Diary(BaseSection):
    def __init__(self, diary: DisplayDiary):
        self.diary = diary
        super().__init__()

    def make(self) -> LatexObject:
        diary_items = Itemize()
        for time, item in self.diary.root.items():
            diary_items.append(Item([], [Bold(time)]))
            diary_items.append(item)
        return diary_items
