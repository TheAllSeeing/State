from pydantic import BaseModel, RootModel, model_validator

from statements.io.statement_providers.config_file.progress_status.progress_status import InputProgressStatus
from statements.io.statement_providers.config_file.validation_types import ID, ProjectName


class InputGoal(BaseModel):
    description: str
    note: str | None = None
    status: InputProgressStatus

    @model_validator(mode='after')
    def ensure_state_if_not_resolved(self):
        if self.status is InputProgressStatus.IN_PROGRESS and not self.note:
            raise ValueError('Note must be included for in-progress items')
        return self


InputGoals = RootModel[dict[ProjectName, dict[ID, InputGoal]]]
