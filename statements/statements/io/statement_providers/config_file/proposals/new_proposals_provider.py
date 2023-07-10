from pydantic import TypeAdapter

from statements.domain.proposal import Proposal
from statements.io.statement_providers.config_file.proposals.proposals import ProjectProposals
from statements.io.statement_providers.config_file.proposals.provider import ProposalsProvider
from statements.io.statement_providers.config_file.toml_provider import TOMLProvider


class TOMLNewProposalProvider(ProposalsProvider, TOMLProvider):
    def get_proposals(self):
        raw_proposals = self._get_raw_data()
        proposal_config = TypeAdapter(ProjectProposals).validate_python(raw_proposals)
        return [Proposal(project=project,
                         accepted=None,
                         description=proposal)
                for project, project_proposals in proposal_config.items()
                for proposal in project_proposals]
