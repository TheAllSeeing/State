from pylatex import Tabular

from statements.intermidiaries.display.habits.habit_maintenance import DisplayScopeMaintenance, DisplaySeriesMaintenance
from statements.io.statement_compiler.latex.wrappers.group import Group
from statements.io.statement_compiler.latex.wrappers.new_paragraph import NewParagraph
from statements.io.statement_compiler.latex.wrappers.set_text_color import SetTextColor
from statements.io.statement_compiler.latex.models.progress_symbol import ProgressSymbol
from statements.io.statement_compiler.latex.utils.insight import Insight


class HabitMaintenance(Group):
    def __init__(self, habit_maintenance: DisplayScopeMaintenance | DisplaySeriesMaintenance):
        super().__init__()
        self.append(SetTextColor(habit_maintenance.project.color.name))
        self.append(Insight(habit_maintenance.project, habit_maintenance.title))

        if isinstance(habit_maintenance, DisplaySeriesMaintenance):
            table = Tabular('|'.join(['c' for _ in habit_maintenance.series]))
            table.add_row(habit_maintenance.series.keys())
            table.add_row([ProgressSymbol(status) for status in habit_maintenance.series.values()])
        elif isinstance(habit_maintenance, DisplayScopeMaintenance):
            table = Tabular('|'.join(['c' for _ in habit_maintenance.inner_scopes] + ['c']))
            table.add_row([''] + habit_maintenance.inner_scopes)
            table.add_hline()
            for scope in habit_maintenance.outer_scopes:
                full_statuses = [habit_maintenance.maintenance[scope].get(inner_scope)
                                 for inner_scope in habit_maintenance.inner_scopes]
                table.add_row([scope] + [ProgressSymbol(status) if status else ''
                                         for status in full_statuses])
        else:
            raise NotImplementedError(f'Unsupported maintenance type: {habit_maintenance.__class__.__name__}')

        self.append(NewParagraph())
        self.append(table)
