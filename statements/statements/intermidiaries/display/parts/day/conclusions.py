from pydantic import BaseModel

from statements.domain.validation_types import Markdown
from statements.intermidiaries.display.goals.goal import DisplayGoal
from statements.intermidiaries.display.proposals.proposal import DisplayProposal
from statements.intermidiaries.display.tasks.task import DisplayTask


class DisplayDayConclusions(BaseModel):
    new_tasks: list[DisplayTask]
    new_proposals: list[DisplayProposal]
    notes: Markdown
