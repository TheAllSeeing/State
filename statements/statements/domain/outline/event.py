from pydantic import BaseModel


class Event(BaseModel):
    time: str
    project: str
    description: str
