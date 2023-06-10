import itertools

from pydantic import Field, BaseModel


class InputAspect(BaseModel):
    rgb: tuple[float, float, float]
    active_projects: list[str] = Field(alias='active')
    passive_projects: list[str] = Field(alias='passive')
    frozen_projects: list[str] = Field(alias='frozen')
    archived_projects: list[str] = Field(alias='archived')
