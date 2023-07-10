from abc import ABC
from enum import Enum

from statements.domain.proposal import Proposal
from statements.io.statement_providers.config_file.proposals.proposals import ProposalConfig
from statements.io.statement_providers.config_file.toml_provider import TOMLProvider


class ResolvedStatus(Enum):
    OPEN = 'open'
    ACCEPTED = 'accepted'
    REJECTED = 'rejected'


STATUS_TO_RESOLVED = {
    ResolvedStatus.OPEN: None,
    ResolvedStatus.REJECTED: False,
    ResolvedStatus.ACCEPTED: True
}


class ProposalsProvider(ABC):
    def get_proposals(self) -> list[Proposal]:
        pass


class TOMLProposalProvider(ProposalsProvider, TOMLProvider):
    def get_proposals(self):
        raw_proposals = self._get_raw_data()
        proposal_config = ProposalConfig.model_validate(raw_proposals)
        return [Proposal(project=project,
                         accepted=STATUS_TO_RESOLVED[ResolvedStatus(status)],
                         description=proposal)
                for status, projects_proposals in proposal_config
                for project, project_proposals in projects_proposals.items()
                for proposal in project_proposals]
