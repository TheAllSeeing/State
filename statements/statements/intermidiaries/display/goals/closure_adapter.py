from statements.domain.goals.goal_closure import GoalClosure
from statements.domain.settings.aspect import Aspect
from statements.intermidiaries.display.goals.adapter import GoalAdapter
from statements.intermidiaries.display.goals.goal_closure import DisplayGoalClosure


class GoalClosureAdapter:
    def __init__(self, goal_adapter: GoalAdapter):
        self.goal_adapter = goal_adapter

    def get_display_goal_closure(self, goal_closure: GoalClosure, projects_to_aspects: dict[str, Aspect]) \
            -> DisplayGoalClosure:
        return DisplayGoalClosure(
            goal=self.goal_adapter.get_display_goal(goal_closure.goal, projects_to_aspects),
            reason=goal_closure.reason
        )
