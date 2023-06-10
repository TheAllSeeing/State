from pydantic import BaseModel


class LatexFontConfig(BaseModel):
    font_family: str
