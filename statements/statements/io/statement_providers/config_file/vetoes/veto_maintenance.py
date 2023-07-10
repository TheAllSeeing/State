from datetime import date

from pydantic import BaseModel, Field, RootModel

from statements.io.statement_providers.config_file.validation_types import ID


class InputVetoViolation(BaseModel):
    date_: date = Field(alias='date')
    detail: str


class InputVetoMaintenance(RootModel):
    root: dict[ID, list[InputVetoViolation]]
