from pylatex import Itemize
from pylatex.base_classes import LatexObject

from statements.intermidiaries.display.habits.habit_maintenance import DisplayScopeMaintenance, DisplaySeriesMaintenance
from statements.io.statement_compiler.latex.models.habit_maintenance import \
    HabitMaintenance as HabitMaintenanceItem
from statements.io.statement_compiler.latex.sections.base_section import BaseSection


class HabitMaintenance(BaseSection):
    def __init__(self, habit_maintenance: list[DisplayScopeMaintenance | DisplaySeriesMaintenance]):
        self.habit_maintenance = habit_maintenance
        super().__init__()

    def make(self) -> LatexObject:
        maintenance_list = Itemize()
        for maintenance in self.habit_maintenance:
            maintenance_list.add_item(HabitMaintenanceItem(maintenance))
        return maintenance_list
