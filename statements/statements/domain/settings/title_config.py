from pydantic import BaseModel


class TitleConfig(BaseModel):
    title: str
    themes: list[str]
    scope: str
