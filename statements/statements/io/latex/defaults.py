from statements.io.latex.latex_objects.spacing_config import Spacing
from statements.io.latex.models.spacing_config import LatexSpacingConfig
from statements.io.latex.models.style import StatementStyle
from statements.io.latex.models.color import LatexColor
from statements.io.latex.models.color_config import LatexColorConfig
from statements.io.latex.models.font_config import LatexFontConfig

DEFAULT_STYLE = StatementStyle(
    spacing_config=LatexSpacingConfig(
        paragraph_indent=0,
        paragraph_skip=1,
        array_stretch=1.5
    ),
    color_config=LatexColorConfig(
        text_color=LatexColor(name='TextColor', red=217, blue=217, green=217),
        page_color=LatexColor(name='PageColor', red=82, blue=82, green=82),
    ),
    font_config=LatexFontConfig(
        font_family='charter'
    )
)
