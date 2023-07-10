from pydantic import BaseModel

from statements.io.statement_providers.config_file.validation_types import ProjectName


class InputEvent(BaseModel):
    time: str
    project: ProjectName
    description: str
