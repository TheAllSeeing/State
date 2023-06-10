from statements.domain.statement import Statement
from statements.providers.aspects import AspectsProvider
from statements.providers.outline import OutlineProvider
from statements.providers.statement_settings import StatementSettingsProvider


class StatementProvider:
    def __init__(self, settings_provider: StatementSettingsProvider, aspects_provider: AspectsProvider,
                 outline_provider: OutlineProvider):
        self.settings_provider = settings_provider
        self.aspects_provider = aspects_provider
        self.outline_provider = outline_provider

    def get_statement(self):
        return Statement(
            config=self.settings_provider.get_statement_settings(),
            aspects=self.aspects_provider.get_aspects(),
            outline=self.outline_provider.get_outline()
        )
