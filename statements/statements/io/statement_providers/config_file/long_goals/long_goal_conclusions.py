from pydantic import BaseModel, Field

from statements.domain.validation_types import ID
from statements.io.statement_providers.config_file.long_goals.long_goal import InputLongGoal


class InputLongGoalClosure(BaseModel):
    reason: str


class InputLongGoalConclusions(BaseModel):
    new: dict[ID, InputLongGoal] = Field(alias='New')
    closed: dict[ID, InputLongGoalClosure] = Field(alias='Closed')