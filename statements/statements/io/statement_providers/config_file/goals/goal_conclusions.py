from pydantic import BaseModel, Field

from statements.domain.validation_types import ID, ProjectName
from statements.io.statement_providers.config_file.goals.goal import InputGoal


class InputGoalClosure(BaseModel):
    reason: str


class InputGoalConclusions(BaseModel):
    new: dict[ID, dict[ProjectName, InputGoal]] = Field(alias='New')
    closed: dict[ID, InputGoalClosure] = Field(alias='Closed')