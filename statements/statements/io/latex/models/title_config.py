from pydantic import BaseModel


class LatexTitleConfig(BaseModel):
    title: str
    themes: str
    scope: str

