from pylatex.base_classes import LatexObject
from pylatex.base_classes.containers import Fragment
from pylatex.basic import TextColor

from statements.intermidiaries.display.projects.project import DisplayProject
from statements.io.statement_compiler.latex.wrappers.bare_container import BareContainer
from statements.io.statement_compiler.latex.wrappers.underline import Underline


class Insight(Fragment):

    def __init__(self, project: DisplayProject, content: LatexObject | str, id_: str = None):
        super().__init__()

        fragment = BareContainer()
        if id_:
            fragment.append(Underline(id_))
            fragment.append(' ')

        fragment.append(f'[{project.name}] ')
        fragment.append(content)

        self.append(TextColor(project.color.name, fragment))
