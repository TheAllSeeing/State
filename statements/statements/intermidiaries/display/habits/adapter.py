from statements.domain.settings.aspect import Aspect
from statements.domain.habits.habit import Habit
from statements.intermidiaries.display.projects.adapter import ProjectAdapter
from statements.intermidiaries.display.habits.habit import DisplayHabit


class HabitAdapter:
    def __init__(self, project_adapter: ProjectAdapter):
        self.project_adapter = project_adapter

    def get_display_habit(self, habit: Habit, projects_to_aspects: dict[str, Aspect]) -> DisplayHabit:
        return DisplayHabit(
            id_=habit.id_,
            project=self.project_adapter.get_display_project(habit.project, projects_to_aspects),
            description=habit.description,
            frequency=habit.frequency.scope.value,
            count=habit.frequency.count,
            hop=habit.frequency.hop
        )
