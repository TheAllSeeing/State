from pydantic import BaseModel


class InputTitleConfig(BaseModel):
    title: str
    themes: list[str]
    scope: str
