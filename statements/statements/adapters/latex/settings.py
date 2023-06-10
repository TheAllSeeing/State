from statements.domain.settings.statement import StatementConfig
from statements.domain.settings.title_config import TitleConfig
from statements.io.latex.models.title_config import LatexTitleConfig


class TitleConfigAdapter:
    def get_latex_title_config(self, config: TitleConfig) -> LatexTitleConfig:
        return LatexTitleConfig(
            title=config.title,
            themes=' | '.join(config.themes),
            scope=config.scope
        )
