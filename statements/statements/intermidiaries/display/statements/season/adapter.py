from statements.domain.statements.season_statement import SeasonStatement
from statements.intermidiaries.display.settings.aspect_adapter import AspectAdapter
from statements.intermidiaries.display.settings.title_config_adapter import TitleConfigAdapter
from statements.intermidiaries.display.parts.season.conclusions_adapter import SeasonConclusionsAdapter
from statements.intermidiaries.display.parts.season.outline_adapter import SeasonOutlineAdapter
from statements.intermidiaries.display.parts.season.results_adapter import SeasonResultsAdapter
from statements.intermidiaries.display.parts.season.status_adapter import SeasonStatusAdapter
from statements.intermidiaries.display.statements.season.statement import DisplaySeasonStatement
from statements.intermidiaries.display.settings.style import DisplayStatementStyle


class SeasonStatementAdapter:
    def __init__(self, aspects_adapter: AspectAdapter,
                 outline_adapter: SeasonOutlineAdapter, status_adapter: SeasonStatusAdapter,
                 results_adapter: SeasonResultsAdapter, conclusions_adapter: SeasonConclusionsAdapter,
                 title_adapter: TitleConfigAdapter, statement_style: DisplayStatementStyle):
        self.aspects_adapter = aspects_adapter
        self.outline_adapter = outline_adapter
        self.status_adapter = status_adapter
        self.results_adapter = results_adapter
        self.conclusions_adapter = conclusions_adapter
        self.title_adapter = title_adapter
        self.statement_style = statement_style

    def get_display_statement(self, statement: SeasonStatement):
        return DisplaySeasonStatement(
            aspects=[self.aspects_adapter.get_display_aspect(aspect) for aspect in statement.aspects],
            title_config=self.title_adapter.get_display_title_config(statement.config.title),
            outline=self.outline_adapter.get_display_outline(statement),
            status=self.status_adapter.get_display_status(statement),
            results=self.results_adapter.get_display_results(statement),
            conclusions=self.conclusions_adapter.get_display_conclusions(statement),
            style=self.statement_style
        )
