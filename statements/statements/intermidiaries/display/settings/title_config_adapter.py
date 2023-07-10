from statements.domain.settings.title_config import TitleConfig
from statements.intermidiaries.display.settings.title_config import DisplayTitleConfig


class TitleConfigAdapter:
    def get_display_title_config(self, config: TitleConfig) -> DisplayTitleConfig:
        return DisplayTitleConfig(
            title=config.title,
            themes=' | '.join(config.themes),
            scope=config.scope
        )
