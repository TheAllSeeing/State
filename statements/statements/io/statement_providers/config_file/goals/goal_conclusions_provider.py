from abc import ABC, abstractmethod
from pathlib import Path

from pydantic import BaseModel

from statements.domain.goals.goal_closure import GoalClosure
from statements.domain.goals.goal import Goal
from statements.domain.validation_types import ID
from statements.io.statement_providers.config_file.goals.adapter import InputGoalAdapter
from statements.io.statement_providers.config_file.goals.goal_conclusions import InputGoalConclusions
from statements.io.statement_providers.config_file.toml_provider import TOMLProvider


class GoalConclusions(BaseModel):
    new_goals: list[Goal]
    goal_closures: list[GoalClosure]


class GoalConclusionsProvider(ABC):
    @abstractmethod
    def get_goal_conclusions(self, outline_goals: dict[ID, Goal]) -> GoalConclusions:
        pass


class TOMLGoalConclusionsProvider(GoalConclusionsProvider, TOMLProvider):
    def __init__(self, file_path: Path, goals_adapter: InputGoalAdapter):
        super().__init__(file_path)
        self.goal_adapter = goals_adapter
        self.goal_adapter = goals_adapter

    def get_goal_conclusions(self, outline_goals: dict[ID, Goal]) -> GoalConclusions:
        raw_data = self._get_raw_data()
        input_conclusions = InputGoalConclusions.model_validate(raw_data)
        return GoalConclusions(
            new_goals=self.goal_adapter.get_domain_goals(input_conclusions.new),
            goal_closures=[
                GoalClosure(
                    goal=outline_goals[id_],
                    reason=closure.reason
                )
                for id_, closure in input_conclusions.closed.items()
            ]
        )
