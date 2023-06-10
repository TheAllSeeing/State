from pydantic import BaseModel, Field


class InputLongGoal(BaseModel):
    id_: str = Field(alias='_id')
    projects: list[str]
    description: str
