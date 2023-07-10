from pydantic import BaseModel

from statements.domain.settings.scope import StatementScope
from statements.domain.settings.title_config import TitleConfig


class StatementConfig(BaseModel):
    title: TitleConfig
    scope: StatementScope
