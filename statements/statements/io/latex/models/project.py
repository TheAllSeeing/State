from pydantic import BaseModel
from statements.io.latex.models.color import LatexColor

class LatexProject(BaseModel):
    color: LatexColor
    name: str