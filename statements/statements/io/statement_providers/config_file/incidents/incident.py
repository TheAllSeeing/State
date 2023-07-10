from pydantic import Field, TypeAdapter, BaseModel


class InputIncident(BaseModel):
    id_: str = Field(alias='id')
    title: str
    description: str


IncidentsConfig = TypeAdapter(dict[str, list[InputIncident]])
