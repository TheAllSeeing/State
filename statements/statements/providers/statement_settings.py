import tomllib
from abc import ABC, abstractmethod
from pathlib import Path

from statements.io.config.statement import InputStatementConfig
from statements.domain.settings.statement import StatementConfig


class StatementSettingsProvider(ABC):
    @abstractmethod
    def get_statement_settings(self) -> StatementConfig:
        pass


class TOMLStatementSettingsProvider(StatementSettingsProvider):
    def __init__(self, file_path: Path):
        self.file_path = file_path

    def get_statement_settings(self) -> StatementConfig:
        with open(self.file_path, 'rb') as aspects_file:
            raw_config = tomllib.load(aspects_file)
        input_config = InputStatementConfig.parse_obj(raw_config)
        return StatementConfig.parse_obj(input_config.dict())
