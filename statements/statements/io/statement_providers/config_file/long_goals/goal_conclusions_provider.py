from abc import ABC, abstractmethod
from pathlib import Path

from pydantic import BaseModel

from statements.domain.long_goals.goal_closure import LongGoalClosure
from statements.domain.long_goals.long_goal import LongGoal
from statements.domain.validation_types import ID
from statements.io.statement_providers.config_file.long_goals.adapter import InputLongGoalAdapter
from statements.io.statement_providers.config_file.long_goals.long_goal_conclusions import InputLongGoalConclusions
from statements.io.statement_providers.config_file.toml_provider import TOMLProvider


class LongGoalConclusions(BaseModel):
    new_goals: list[LongGoal]
    goal_closures: list[LongGoalClosure]


class LongGoalConclusionsProvider(ABC):
    @abstractmethod
    def get_goal_conclusions(self, outline_goals: dict[ID, LongGoal]) -> LongGoalConclusions:
        pass


class TOMLLongGoalConclusionsProvider(LongGoalConclusionsProvider, TOMLProvider):
    def __init__(self, file_path: Path, goals_adapter: InputLongGoalAdapter):
        super().__init__(file_path)
        self.goal_adapter = goals_adapter
        self.goal_adapter = goals_adapter

    def get_goal_conclusions(self, outline_goals: dict[ID, LongGoal]) -> LongGoalConclusions:
        raw_data = self._get_raw_data()
        input_conclusions = InputLongGoalConclusions.model_validate(raw_data)
        return LongGoalConclusions(
            new_goals=self.goal_adapter.get_domain_goals(input_conclusions.new),
            goal_closures=[
                LongGoalClosure(
                    goal=outline_goals[id_],
                    reason=closure.reason
                )
                for id_, closure in input_conclusions.closed.items()
            ]
        )
