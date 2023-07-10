from statements.domain.settings.aspect import Aspect
from statements.domain.proposal import Proposal
from statements.intermidiaries.display.projects.adapter import ProjectAdapter
from statements.intermidiaries.display.proposals.proposal import DisplayProposal, DisplayProposalStatus


class ProposalAdapter:
    def __init__(self, project_adapter: ProjectAdapter):
        self.project_adapter = project_adapter

    def get_display_proposal_status(self, accepted: bool | None) -> DisplayProposalStatus | None:
        if accepted is None:
            return None
        elif accepted:
            return DisplayProposalStatus.ACCEPTED
        else:
            return DisplayProposalStatus.REJECTED

    def get_display_proposal(self, proposal: Proposal, projects_to_aspects: dict[str, Aspect]):
        return DisplayProposal(
            project=self.project_adapter.get_display_project(proposal.project, projects_to_aspects),
            status=self.get_display_proposal_status(proposal.accepted),
            description=proposal.description
        )
