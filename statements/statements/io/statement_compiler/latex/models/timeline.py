from pylatex import Package, NoEscape
from pylatex.base_classes import Environment

from statements.consts import RESOURCES_DIR
from statements.intermidiaries.display.events.event import DisplayEvent
from statements.io.statement_compiler.latex.utils.insight import Insight


class Timeline(Environment):
    packages = [Package(NoEscape(f'{RESOURCES_DIR}/timeline'))]
    _latex_name = 'timeline'
    content_separator = ' '

    def __init__(self, *, color: str = None, **kwargs):
        super().__init__(options=f'color={color}' if color else None, **kwargs)

    def append(self, item: DisplayEvent) -> None:
        self.data.append(item.time)
        self.data.append(NoEscape('&'))
        self.data.append(Insight(project=item.project, content=item.description))
        self.data.append(NoEscape('\\endlr\n'))
