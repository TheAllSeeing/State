from pydantic import BaseModel

from statements.io.statement_providers.config_file.settings.scope import InputScope
from statements.io.statement_providers.config_file.settings.title_config import InputTitleConfig


class InputStatementConfig(BaseModel):
    title: InputTitleConfig
    scope: InputScope
