from pydantic import BaseModel

from statements.io.latex.models.project import LatexProject


class LatexEvent(BaseModel):
    time: str
    project: LatexProject
    description: str
