from abc import ABC, abstractmethod
from pathlib import Path

from statements.domain.goals.goal import Goal
from statements.io.statement_providers.config_file.goals.adapter import InputGoalAdapter
from statements.io.statement_providers.config_file.progress_status.adapter import InputProgressStatusAdapter
from statements.io.statement_providers.config_file.goals.goal import InputGoals
from statements.io.statement_providers.config_file.toml_provider import TOMLProvider


class GoalsProvider(ABC):
    @abstractmethod
    def get_goals(self) -> list[Goal]:
        pass


class TOMLGoalsProvider(GoalsProvider, TOMLProvider):
    def __init__(self, file_path: Path, goal_adapter: InputGoalAdapter):
        super().__init__(file_path)
        self.goal_adapter = goal_adapter

    def get_goals(self) -> list[Goal]:
        raw_goals = self._get_raw_data()
        input_goals = InputGoals.model_validate(raw_goals).root
        return self.goal_adapter.get_domain_goals(input_goals)
