from statements.domain.statements.day_statement import DailyStatement
from statements.intermidiaries.display.parts.day.conclusions_adapter import DayConclusionsAdapter
from statements.intermidiaries.display.parts.day.outline_adapter import DayOutlineAdapter
from statements.intermidiaries.display.parts.day.results_adapter import DayResultsAdapter
from statements.intermidiaries.display.parts.day.status_adapter import DayStatusAdapter
from statements.intermidiaries.display.settings.aspect_adapter import AspectAdapter
from statements.intermidiaries.display.settings.title_config_adapter import TitleConfigAdapter
from statements.intermidiaries.display.statements.day.statement import DisplayDailyStatement
from statements.intermidiaries.display.settings.style import DisplayStatementStyle


class DailyStatementAdapter:
    def __init__(self, aspects_adapter: AspectAdapter,
                 outline_adapter: DayOutlineAdapter, status_adapter: DayStatusAdapter,
                 results_adapter: DayResultsAdapter, conclusions_adapter: DayConclusionsAdapter,
                 title_adapter: TitleConfigAdapter, statement_style: DisplayStatementStyle):
        self.aspects_adapter = aspects_adapter
        self.outline_adapter = outline_adapter
        self.status_adapter = status_adapter
        self.results_adapter = results_adapter
        self.conclusions_adapter = conclusions_adapter
        self.title_adapter = title_adapter
        self.statement_style = statement_style

    def get_display_statement(self, statement: DailyStatement):
        return DisplayDailyStatement(
            aspects=[self.aspects_adapter.get_display_aspect(aspect) for aspect in statement.aspects],
            title_config=self.title_adapter.get_display_title_config(statement.config.title),
            outline=self.outline_adapter.get_display_outline(statement),
            status=self.status_adapter.get_display_status(statement),
            results=self.results_adapter.get_display_results(statement),
            conclusions=self.conclusions_adapter.get_display_conclusions(statement),
            style=self.statement_style
        )
