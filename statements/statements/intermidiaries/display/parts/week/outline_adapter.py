from statements.domain.statements.week_statement import WeeklyStatement
from statements.intermidiaries.display.events.adapter import EventAdapter
from statements.intermidiaries.display.habits.adapter import HabitAdapter
from statements.intermidiaries.display.goals.adapter import GoalAdapter
from statements.intermidiaries.display.tasks.adapter import TaskAdapter
from statements.intermidiaries.display.vetoes.adapter import VetoAdapter
from statements.intermidiaries.display.parts.week.outline import DisplayWeekOutline


class WeekOutlineAdapter:
    def __init__(self, goal_adapter: GoalAdapter, event_adapter: EventAdapter,
                 habit_adapter: HabitAdapter, veto_adapter: VetoAdapter, task_adapter: TaskAdapter):
        self.goal_adapter = goal_adapter
        self.event_adapter = event_adapter
        self.habit_adapter = habit_adapter
        self.veto_adapter = veto_adapter
        self.task_adapter = task_adapter

    def get_display_outline(self, statement: WeeklyStatement) -> DisplayWeekOutline:
        return DisplayWeekOutline(
            schedule=[self.event_adapter.get_display_event(event, statement.projects_to_aspects)
                      for event in statement.schedule],
            goals=[self.goal_adapter.get_display_goal(goal, statement.projects_to_aspects)
                   for goal in statement.goals],
            habits=[self.habit_adapter.get_display_habit(habit, statement.projects_to_aspects)
                    for habit in statement.habits],
            vetoes=[self.veto_adapter.get_display_veto(veto, statement.projects_to_aspects)
                    for veto in statement.vetoes],
            tasks=[self.task_adapter.get_display_task(task, statement.projects_to_aspects)
                   for task in statement.tasks],
            plan=[self.event_adapter.get_display_event(event, statement.projects_to_aspects)
                  for event in statement.timeline]
        )
