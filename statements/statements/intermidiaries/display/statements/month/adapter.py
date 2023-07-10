from statements.domain.statements.month_statement import MonthlyStatement
from statements.intermidiaries.display.parts.month.conclusions_adapter import MonthConclusionsAdapter
from statements.intermidiaries.display.parts.month.outline_adapter import MonthOutlineAdapter
from statements.intermidiaries.display.parts.month.results_adapter import MonthResultsAdapter
from statements.intermidiaries.display.parts.month.status_adapter import MonthStatusAdapter
from statements.intermidiaries.display.settings.aspect_adapter import AspectAdapter
from statements.intermidiaries.display.settings.title_config_adapter import TitleConfigAdapter
from statements.intermidiaries.display.statements.month.statement import DisplayMonthlyStatement
from statements.intermidiaries.display.settings.style import DisplayStatementStyle


class MonthStatementAdapter:
    def __init__(self, aspects_adapter: AspectAdapter,
                 outline_adapter: MonthOutlineAdapter, status_adapter: MonthStatusAdapter,
                 results_adapter: MonthResultsAdapter, conclusions_adapter: MonthConclusionsAdapter,
                 title_adapter: TitleConfigAdapter, statement_style: DisplayStatementStyle):
        self.aspects_adapter = aspects_adapter
        self.outline_adapter = outline_adapter
        self.status_adapter = status_adapter
        self.results_adapter = results_adapter
        self.conclusions_adapter = conclusions_adapter
        self.title_adapter = title_adapter
        self.statement_style = statement_style

    def get_display_statement(self, statement: MonthlyStatement):
        return DisplayMonthlyStatement(
            aspects=[self.aspects_adapter.get_display_aspect(aspect) for aspect in statement.aspects],
            title_config=self.title_adapter.get_display_title_config(statement.config.title),
            outline=self.outline_adapter.get_display_outline(statement),
            status=self.status_adapter.get_display_status(statement),
            results=self.results_adapter.get_display_results(statement),
            conclusions=self.conclusions_adapter.get_display_conclusions(statement),
            style=self.statement_style
        )
