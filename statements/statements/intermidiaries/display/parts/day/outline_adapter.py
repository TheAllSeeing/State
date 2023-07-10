from statements.domain.statements.day_statement import DailyStatement
from statements.intermidiaries.display.events.adapter import EventAdapter
from statements.intermidiaries.display.habits.adapter import HabitAdapter
from statements.intermidiaries.display.goals.adapter import GoalAdapter
from statements.intermidiaries.display.tasks.adapter import TaskAdapter
from statements.intermidiaries.display.vetoes.adapter import VetoAdapter
from statements.intermidiaries.display.parts.day.outline import DisplayDayOutline


class DayOutlineAdapter:
    def __init__(self, event_adapter: EventAdapter, veto_adapter: VetoAdapter, task_adapter: TaskAdapter):
        self.event_adapter = event_adapter
        self.veto_adapter = veto_adapter
        self.task_adapter = task_adapter

    def get_display_outline(self, statement: DailyStatement) -> DisplayDayOutline:
        return DisplayDayOutline(
            schedule=[self.event_adapter.get_display_event(event, statement.projects_to_aspects)
                      for event in statement.schedule],
            vetoes=[self.veto_adapter.get_display_veto(veto, statement.projects_to_aspects)
                    for veto in statement.vetoes],
            tasks=[self.task_adapter.get_display_task(task, statement.projects_to_aspects)
                   for task in statement.tasks],
            plan=[self.event_adapter.get_display_event(event, statement.projects_to_aspects)
                  for event in statement.timeline]
        )
