from pydantic import BaseModel


class DisplayColor(BaseModel):
    name: str
    red: float
    green: float
    blue: float
