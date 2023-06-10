from pydantic import BaseModel

from statements.io.latex.models.color import LatexColor
from statements.io.latex.models.project import LatexProject


class LatexAspect(BaseModel):
    name: str
    color: LatexColor
    active_projects: list[LatexProject]
    passive_projects: list[LatexProject]
    frozen_projects: list[LatexProject]
    archived_projects: list[LatexProject]
