from pydantic import BaseModel, Field

from statements.domain.validation_types import Markdown


class InputIssue(BaseModel):
    id_: str = Field(alias='id')
    title: str
    description: Markdown | None = None
    note: Markdown | None = None
    resolved: bool = False
