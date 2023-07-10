from pydantic import BaseModel


class DisplayFontConfig(BaseModel):
    font_family: str
