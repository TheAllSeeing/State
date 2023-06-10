from pylatex import Package, NoEscape
from pylatex.base_classes import Environment

from statements.io.latex.latex_objects.insight import Insight
from statements.io.latex.models.event import LatexEvent


class Timeline(Environment):
    packages = [Package('resources/timeline')]
    _latex_name = 'Timeline'
    content_separator = r' '

    def append(self, item: LatexEvent) -> None:
        self.data.append(item)
        self.data.append(item.time)
        self.data.append(NoEscape('&'))
        self.data.append(Insight(project=item.project, content=item.description))
        self.data.append(r'\\' + '\n')
