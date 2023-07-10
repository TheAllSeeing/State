from statements.domain.long_goals.goal_closure import LongGoalClosure
from statements.domain.settings.aspect import Aspect
from statements.intermidiaries.display.long_goals.adapter import LongGoalAdapter
from statements.intermidiaries.display.long_goals.goal_closure import DisplayLongGoalClosure


class LongGoalClosureAdapter:
    def __init__(self, goal_adapter: LongGoalAdapter):
        self.goal_adapter = goal_adapter

    def get_display_goal_closure(self, goal_closure: LongGoalClosure, projects_to_aspects: dict[str, Aspect]) -> DisplayLongGoalClosure:
        return DisplayLongGoalClosure(
            goal=self.goal_adapter.get_display_goal(goal_closure.goal, projects_to_aspects),
            reason=goal_closure.reason
        )
