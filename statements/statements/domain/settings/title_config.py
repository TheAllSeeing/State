from pydantic import BaseModel
from pylatex import Command, Document


class TitleConfig(BaseModel):
    title: str
    themes: list[str]
    scope: str
