from statements.domain.statements.week_statement import WeeklyStatement
from statements.intermidiaries.display.parts.week.conclusions_adapter import WeekConclusionsAdapter
from statements.intermidiaries.display.parts.week.outline_adapter import WeekOutlineAdapter
from statements.intermidiaries.display.parts.week.results_adapter import WeekResultsAdapter
from statements.intermidiaries.display.parts.week.status_adapter import WeekStatusAdapter
from statements.intermidiaries.display.settings.aspect_adapter import AspectAdapter
from statements.intermidiaries.display.settings.title_config_adapter import TitleConfigAdapter
from statements.intermidiaries.display.statements.week.statement import DisplayWeeklyStatement
from statements.intermidiaries.display.settings.style import DisplayStatementStyle


class WeeklyStatementAdapter:
    def __init__(self, aspects_adapter: AspectAdapter,
                 outline_adapter: WeekOutlineAdapter, status_adapter: WeekStatusAdapter,
                 results_adapter: WeekResultsAdapter, conclusions_adapter: WeekConclusionsAdapter,
                 title_adapter: TitleConfigAdapter, statement_style: DisplayStatementStyle):
        self.aspects_adapter = aspects_adapter
        self.outline_adapter = outline_adapter
        self.status_adapter = status_adapter
        self.results_adapter = results_adapter
        self.conclusions_adapter = conclusions_adapter
        self.title_adapter = title_adapter
        self.statement_style = statement_style

    def get_display_statement(self, statement: WeeklyStatement):
        return DisplayWeeklyStatement(
            aspects=[self.aspects_adapter.get_display_aspect(aspect) for aspect in statement.aspects],
            title_config=self.title_adapter.get_display_title_config(statement.config.title),
            outline=self.outline_adapter.get_display_outline(statement),
            status=self.status_adapter.get_display_status(statement),
            results=self.results_adapter.get_display_results(statement),
            conclusions=self.conclusions_adapter.get_display_conclusions(statement),
            style=self.statement_style
        )
