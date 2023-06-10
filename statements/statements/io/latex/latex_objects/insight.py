from pylatex.base_classes import LatexObject
from pylatex.basic import TextColor

from statements.io.latex.models.project import LatexProject
from statements.io.latex.utils import BareContainer
from statements.io.latex.utils.underline import Underline


class Insight(LatexObject):

    def __init__(self, project: LatexProject, content: LatexObject | str, id_: str = None):
        super().__init__()
        self.id_ = id_
        self.project = project
        self.content = content

    def dumps(self):
        container = BareContainer()
        if self.id_:
            container.append(Underline(self.id_))

        container.append(f'[{self.project.name}]')
        if isinstance(self.content, LatexObject):
            container.append(self.content.dumps())
        else:
            container.append(self.content)

        return TextColor(self.project.color.name, container).dumps()
