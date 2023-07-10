from statements.domain.goals.goal import Goal
from statements.domain.settings.aspect import Aspect
from statements.intermidiaries.display.goals.goal import DisplayGoal
from statements.intermidiaries.display.progress_status.adapter import ProgressStatusAdapter
from statements.intermidiaries.display.projects.adapter import ProjectAdapter


class GoalAdapter:
    def __init__(self, project_adapter: ProjectAdapter, progress_status_adapter: ProgressStatusAdapter):
        self.project_adapter = project_adapter
        self.status_adapter = progress_status_adapter

    def get_display_goal(self, goal: Goal, projects_to_aspects: dict[str, Aspect]) -> DisplayGoal:
        return DisplayGoal(
            id_=goal.id_,
            project=self.project_adapter.get_display_project(goal.project, projects_to_aspects),
            description=goal.description,
            status=self.status_adapter.get_progress_status(goal.status),
            note=goal.note
        )
