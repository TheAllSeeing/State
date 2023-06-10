import json
from abc import ABC, abstractmethod
from pathlib import Path

from pydantic import parse_obj_as, TypeAdapter

from statements.io.config.long_goal import InputLongGoal
from statements.domain.outline.long_goal import LongGoal


class LongGoalProvider(ABC):
    @abstractmethod
    def get_long_goals(self) -> list[LongGoal]:
        pass


class JSONLongGoalProvider(LongGoalProvider):
    def __init__(self, file_path: Path):
        self.file_path = file_path

    def get_long_goals(self) -> list[LongGoal]:
        with open(self.file_path, 'r') as goals_file:
            raw_goals = json.load(goals_file)
        input_goals = TypeAdapter(list[InputLongGoal]).validate_python(raw_goals)
        return TypeAdapter(list[LongGoal]).validate_python([goal.dict() for goal in input_goals])
