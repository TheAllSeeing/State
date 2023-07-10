from pylatex import Itemize
from pylatex.base_classes.containers import Fragment

from statements.intermidiaries.display.vetoes.veto_maintenance import DisplayVetoMaintenance
from statements.io.statement_compiler.latex.wrappers import TextBF as Bold
from statements.io.statement_compiler.latex.wrappers.group import Group
from statements.io.statement_compiler.latex.wrappers.set_text_color import SetTextColor
from statements.io.statement_compiler.latex.utils.insight import Insight


class VetoMaintenance(Group):
    def __init__(self, veto_maintenance: DisplayVetoMaintenance):
        super().__init__()
        self.append(SetTextColor(veto_maintenance.project.color.name))
        self.append(Insight(veto_maintenance.project, veto_maintenance.title))
        with self.create(Itemize()) as violations_list:
            for violation in veto_maintenance.violations:
                fragment = Fragment()
                fragment.append(Bold(f'{violation.time_point}: '))
                fragment.append(violation.detail)
                violations_list.add_item(fragment)
