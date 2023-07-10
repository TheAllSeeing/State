from pylatex import Itemize
from pylatex.base_classes import LatexObject

from statements.intermidiaries.display.vetoes.veto_maintenance import DisplayVetoMaintenance
from statements.io.statement_compiler.latex.models.veto_maintenance import \
    VetoMaintenance as VetoMaintenanceItem
from statements.io.statement_compiler.latex.sections.base_section import BaseSection


class VetoMaintenance(BaseSection):
    def __init__(self, veto_maintenance: list[DisplayVetoMaintenance]):
        self.veto_maintenance = veto_maintenance
        super().__init__()

    def make(self) -> LatexObject:
        maintenance_list = Itemize()
        for veto in self.veto_maintenance:
            maintenance_list.add_item(VetoMaintenanceItem(veto))
        return maintenance_list
