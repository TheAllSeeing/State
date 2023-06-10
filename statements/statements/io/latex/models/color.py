from pydantic import BaseModel


class LatexColor(BaseModel):
    name: str
    red: float
    green: float
    blue: float
