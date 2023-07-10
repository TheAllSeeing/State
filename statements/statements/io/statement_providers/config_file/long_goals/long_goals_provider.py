from abc import ABC, abstractmethod
from pathlib import Path

from statements.domain.long_goals.long_goal import LongGoal
from statements.io.statement_providers.config_file.long_goals.adapter import InputLongGoalAdapter
from statements.io.statement_providers.config_file.progress_status.adapter import InputProgressStatusAdapter
from statements.io.statement_providers.config_file.long_goals.long_goal import InputLongGoals
from statements.io.statement_providers.config_file.toml_provider import TOMLProvider


class LongGoalProvider(ABC):
    @abstractmethod
    def get_long_goals(self) -> list[LongGoal]:
        pass


class TOMLLongGoalProvider(LongGoalProvider, TOMLProvider):
    def __init__(self, file_path: Path, goal_adapter: InputLongGoalAdapter):
        super().__init__(file_path)
        self.goal_adapter = goal_adapter

    def get_long_goals(self) -> list[LongGoal]:
        raw_goals = self._get_raw_data()
        input_goals = InputLongGoals.model_validate(raw_goals).root
        return self.goal_adapter.get_domain_goals(input_goals)
