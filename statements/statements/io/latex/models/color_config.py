from pydantic import BaseModel

from statements.io.latex.models.color import LatexColor


class LatexColorConfig(BaseModel):
    text_color: LatexColor
    page_color: LatexColor
