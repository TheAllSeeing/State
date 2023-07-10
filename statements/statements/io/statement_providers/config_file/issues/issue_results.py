from pydantic import BaseModel, Field

from statements.io.statement_providers.config_file.issues.issue import InputIssue
from statements.io.statement_providers.config_file.validation_types import ProjectName


class InputIssueResults(BaseModel):
    new: dict[ProjectName, list[InputIssue]] = Field(alias='Opened')
    closed: dict[ProjectName, list[InputIssue]] = Field(alias='Closed')
