from pydantic import BaseModel

from statements.intermidiaries.display.settings.aspect import DisplayAspect
from statements.intermidiaries.display.settings.style import DisplayStatementStyle
from statements.intermidiaries.display.settings.title_config import DisplayTitleConfig


class DisplayStatement(BaseModel):
    aspects: list[DisplayAspect]
    title_config: DisplayTitleConfig
    style: DisplayStatementStyle
