import itertools

from pydantic import Field, BaseModel
from pydantic.color import Color


class Aspect(BaseModel):
    name: str
    color: Color
    active_projects: list[str]
    passive_projects: list[str]
    frozen_projects: list[str]
    archived_projects: list[str]



