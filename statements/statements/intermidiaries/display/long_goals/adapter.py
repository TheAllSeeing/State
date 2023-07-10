from statements.domain.settings.aspect import Aspect
from statements.domain.long_goals.long_goal import LongGoal
from statements.intermidiaries.display.progress_status.adapter import ProgressStatusAdapter
from statements.intermidiaries.display.projects.adapter import ProjectAdapter
from statements.intermidiaries.display.long_goals.long_goal import DisplayLongGoal


class LongGoalAdapter:
    def __init__(self, project_adapter: ProjectAdapter, progress_status_adapter: ProgressStatusAdapter):
        self.project_adapter = project_adapter
        self.status_adapter = progress_status_adapter

    def get_display_goal(self, goal: LongGoal, projects_to_aspects: dict[str, Aspect]) -> DisplayLongGoal:
        return DisplayLongGoal(
            id_=goal.id_,
            color=self.project_adapter.get_display_project(goal.projects[0], projects_to_aspects).color,
            projects=', '.join(goal.projects),
            description=goal.description,
            status=self.status_adapter.get_progress_status(goal.status),
            note=goal.note
        )
