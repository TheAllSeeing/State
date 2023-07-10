from pylatex import Itemize, Subsection
from pylatex.base_classes import LatexObject
from pylatex.base_classes.containers import Fragment

from statements.intermidiaries.display.projects.project_status_change import DisplayProjectStatusChange, \
    DisplayStatusChange
from statements.io.statement_compiler.latex.models.project_status_change import ProjectStatusChange
from statements.io.statement_compiler.latex.sections.base_section import BaseSection


class ProjectStatusChanges(BaseSection):
    _title = 'Projects'

    def __init__(self, project_status_changes: dict[DisplayStatusChange, list[DisplayProjectStatusChange]]):
        self.project_status_changes = project_status_changes
        super().__init__()

    def make(self) -> LatexObject:
        fragment = Fragment()
        for status, change_list in self.project_status_changes.items():
            if change_list:
                with fragment.create(Subsection(status.value, numbering=False)) as status_subsection:
                    with status_subsection.create(Itemize()) as changes_items:
                        for change in change_list:
                            changes_items.add_item(ProjectStatusChange(change))
        return fragment
