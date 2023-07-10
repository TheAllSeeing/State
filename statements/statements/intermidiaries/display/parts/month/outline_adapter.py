from statements.domain.statements.month_statement import MonthlyStatement
from statements.intermidiaries.display.events.adapter import EventAdapter
from statements.intermidiaries.display.habits.adapter import HabitAdapter
from statements.intermidiaries.display.goals.adapter import GoalAdapter
from statements.intermidiaries.display.vetoes.adapter import VetoAdapter
from statements.intermidiaries.display.parts.month.outline import DisplayMonthOutline


class MonthOutlineAdapter:
    def __init__(self, goal_adapter: GoalAdapter, event_adapter: EventAdapter,
                 habit_adapter: HabitAdapter, veto_adapter: VetoAdapter):
        self.goal_adapter = goal_adapter
        self.event_adapter = event_adapter
        self.habit_adapter = habit_adapter
        self.veto_adapter = veto_adapter

    def get_display_outline(self, statement: MonthlyStatement) -> DisplayMonthOutline:
        return DisplayMonthOutline(
            schedule=[self.event_adapter.get_display_event(event, statement.projects_to_aspects) for event in
                      statement.schedule],
            goals=[self.goal_adapter.get_display_goal(goal, statement.projects_to_aspects) for goal in statement.goals],
            habits=[self.habit_adapter.get_display_habit(habit, statement.projects_to_aspects) for habit in
                    statement.habits],
            vetoes=[self.veto_adapter.get_display_veto(veto, statement.projects_to_aspects) for veto in
                    statement.vetoes],
            plan=[self.event_adapter.get_display_event(event, statement.projects_to_aspects) for event in
                  statement.timeline]
        )
