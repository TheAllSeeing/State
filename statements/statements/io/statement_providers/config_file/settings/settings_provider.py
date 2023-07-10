from abc import ABC, abstractmethod
from builtins import getattr

from statements.domain.settings.scope import StatementScope, StatementType
from statements.domain.settings.statement_config import StatementConfig
from statements.domain.settings.title_config import TitleConfig
from statements.io.statement_providers.config_file.settings.statement_config import InputStatementConfig
from statements.io.statement_providers.config_file.toml_provider import TOMLProvider


class StatementSettingsProvider(ABC):
    @abstractmethod
    def get_statement_settings(self) -> StatementConfig:
        pass


class TOMLStatementSettingsProvider(StatementSettingsProvider, TOMLProvider):
    def get_statement_settings(self) -> StatementConfig:
        raw_config = self._get_raw_data()
        input_config = InputStatementConfig.model_validate(raw_config)
        return StatementConfig(
            title=TitleConfig.model_validate(input_config.title.model_dump()),
            scope=StatementScope(
                type_=getattr(StatementType, input_config.scope.type_.name),
                start=input_config.scope.start
            )
        )
