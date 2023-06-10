import itertools
import os
from pathlib import Path

from statements.adapters.latex.aspect import AspectAdapter
from statements.adapters.latex.color import ColorAdapter
from statements.adapters.latex.outline import OutlineAdapter, LongGoalAdapter
from statements.adapters.latex.settings import TitleConfigAdapter
from statements.adapters.latex.statement import StatementAdapter
from statements.providers.aspects import TOMLAspectsProvider
from statements.providers.outline import OutlineProvider
from statements.providers.outline.long_goals import JSONLongGoalProvider
from statements.providers.outline.overview import FileOverviewProvider
from statements.providers.outline.timeline import TOMLTimelineProvider
from statements.providers.statement import StatementProvider
from statements.providers.statement_settings import TOMLStatementSettingsProvider

BASE_DIR = Path(os.getcwd()) / '..' / 'src'
OUTLINE_DIR = BASE_DIR / 'outline'

LATEX_COMPILER = '../.TinyTeX/bin/x86_64-linux/lualatex'

if __name__ == '__main__':
    statement_provider = StatementProvider(
        outline_provider=OutlineProvider(
            overview_provider=FileOverviewProvider(file_path=OUTLINE_DIR / 'overview.md'),
            schedule_provider=TOMLTimelineProvider(file_path=OUTLINE_DIR / 'schedule.toml'),
            goals_provider=JSONLongGoalProvider(file_path=OUTLINE_DIR / 'goals.json')
        ),
        aspects_provider=TOMLAspectsProvider(file_path=BASE_DIR / 'projects.toml'),
        settings_provider=TOMLStatementSettingsProvider(file_path=BASE_DIR / 'statement.toml')
    )

    statement = statement_provider.get_statement()

    color_adapter = ColorAdapter()

    statement_adapter = StatementAdapter(
        outline_adapter=OutlineAdapter(
            goal_adapter=LongGoalAdapter(color_adapter=color_adapter, projects=statement.projects_to_aspects),
        ),
        aspects_adapter=AspectAdapter(color_adapter=color_adapter),
        title_adapter=TitleConfigAdapter()
    )

    statement_adapter.get_latex_statement(statement).build().generate_pdf('Statement', compiler=LATEX_COMPILER,
                                                                          clean_tex=False)
