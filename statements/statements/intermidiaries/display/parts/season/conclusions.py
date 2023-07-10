from pydantic import BaseModel

from statements.domain.validation_types import Markdown
from statements.intermidiaries.display.long_goals.goal_closure import DisplayLongGoalClosure
from statements.intermidiaries.display.long_goals.long_goal import DisplayLongGoal
from statements.intermidiaries.display.projects.project_status_change import DisplayProjectStatusChange, \
    DisplayStatusChange
from statements.intermidiaries.display.proposals.proposal import DisplayProposal


class DisplaySeasonConclusions(BaseModel):
    project_status_changes: dict[DisplayStatusChange, list[DisplayProjectStatusChange]]
    new_goals: list[DisplayLongGoal]
    closed_goals: list[DisplayLongGoalClosure]
    new_proposals: list[DisplayProposal]
    notes: Markdown
