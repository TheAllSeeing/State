from pylatex.utils import bold

from statements.intermidiaries.display.projects.project_status_change import DisplayProjectStatusChange
from statements.io.statement_compiler.latex.wrappers.group import Group
from statements.io.statement_compiler.latex.wrappers.new_paragraph import NewParagraph
from statements.io.statement_compiler.latex.wrappers.set_text_color import SetTextColor


class ProjectStatusChange(Group):
    def __init__(self, status_change: DisplayProjectStatusChange):
        super().__init__()
        self.append(SetTextColor(status_change.project.color.name))
        self.append(bold(status_change.project.name))
        self.append(f'({status_change.project_stub})')
        self.append(NewParagraph())
        self.append(status_change.change_description)