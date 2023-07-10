from statements.domain.goals.goal import Goal
from statements.domain.validation_types import ID, ProjectName
from statements.io.statement_providers.config_file.goals.goal import InputGoal
from statements.io.statement_providers.config_file.progress_status.adapter import InputProgressStatusAdapter


class InputGoalAdapter:
    def __init__(self, status_adapter: InputProgressStatusAdapter):
        self.status_adapter = status_adapter

    def get_domain_goals(self, goals: dict[ID, dict[ProjectName, InputGoal]]) -> list[Goal]:
        return [Goal(id_=id_, project=project, description=goal.description, note=goal.note,
                     status=self.status_adapter.get_progress_status(goal.status))
                for project, project_goals in goals.items()
                for id_, goal in project_goals.items()]
