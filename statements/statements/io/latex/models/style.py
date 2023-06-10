from pydantic import BaseModel

from statements.io.latex.models.color_config import LatexColorConfig
from statements.io.latex.models.font_config import LatexFontConfig
from statements.io.latex.models.spacing_config import LatexSpacingConfig


class StatementStyle(BaseModel):
    font_config: LatexFontConfig
    color_config: LatexColorConfig
    spacing_config: LatexSpacingConfig
