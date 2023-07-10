from pydantic import BaseModel, Field
from typing_extensions import TypeAlias

from statements.io.statement_providers.config_file.validation_types import ProjectName

ProposalDescription: TypeAlias = str

ProjectProposals = dict[ProjectName, list[ProposalDescription]]


class ProposalConfig(BaseModel):
    open: ProjectProposals = Field(alias='Open')
    accepted: ProjectProposals = Field(alias='Accepted')
    rejected: ProjectProposals = Field(alias='Rejected')
