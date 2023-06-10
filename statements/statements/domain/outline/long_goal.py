from pydantic import BaseModel, Field


class LongGoal(BaseModel):
    id_: str
    projects: list[str]
    description: str
