from pydantic import BaseModel


class DisplayTitleConfig(BaseModel):
    title: str
    themes: str
    scope: str

