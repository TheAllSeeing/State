from statements.domain.long_goals.long_goal import LongGoal
from statements.domain.validation_types import ID
from statements.io.statement_providers.config_file.long_goals.long_goal import InputLongGoal
from statements.io.statement_providers.config_file.progress_status.adapter import InputProgressStatusAdapter


class InputLongGoalAdapter:
    def __init__(self, status_adapter: InputProgressStatusAdapter):
        self.status_adapter = status_adapter

    def get_domain_goals(self, goals: dict[ID, InputLongGoal]) -> list[LongGoal]:
        return [LongGoal(id_=id_, projects=goal.projects, description=goal.description, note=goal.note,
                         status=self.status_adapter.get_progress_status(goal.status))
                for id_, goal in goals.items()]
