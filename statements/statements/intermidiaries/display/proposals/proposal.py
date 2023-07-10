from enum import Enum

from pydantic import BaseModel

from statements.intermidiaries.display.projects.project import DisplayProject


class DisplayProposalStatus(Enum):
    ACCEPTED = 'Accepted'
    REJECTED = 'Rejected'


class DisplayProposal(BaseModel):
    project: DisplayProject
    status: DisplayProposalStatus | None
    description: str
