from pylatex.base_classes.containers import Fragment

from statements.intermidiaries.display.day.day import DisplayRestItem
from statements.io.statement_compiler.latex.wrappers import TextBF as Bold


class RestItem(Fragment):
    def __init__(self, rest_item: DisplayRestItem):
        super().__init__()
        self.append(Bold(f'{rest_item.title} | {rest_item.time_range} | '))
        self.append(f'{rest_item.description}')
