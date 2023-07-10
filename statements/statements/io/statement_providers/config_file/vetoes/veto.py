from pydantic import BaseModel, RootModel, Field

from statements.io.statement_providers.config_file.validation_types import ID, ProjectName


class InputVetoData(BaseModel):
    id_: ID = Field(alias='id')
    description: str


class InputVetoes(RootModel):
    root: dict[ProjectName, list[InputVetoData]]
