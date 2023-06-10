from pydantic import BaseModel

from statements.domain.outline.outline import Markdown
from statements.io.latex.models.color import LatexColor


class LatexLongGoal(BaseModel):
    id_: str
    color: LatexColor
    projects: str
    description: Markdown
