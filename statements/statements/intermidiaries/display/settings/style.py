from pydantic import BaseModel

from statements.intermidiaries.display.settings.color_config import DisplayColorConfig
from statements.intermidiaries.display.settings.font_config import DisplayFontConfig
from statements.intermidiaries.display.settings.spacing_config import DisplaySpacingConfig


class DisplayStatementStyle(BaseModel):
    font_config: DisplayFontConfig
    color_config: DisplayColorConfig
    spacing_config: DisplaySpacingConfig
