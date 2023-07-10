from pylatex import Itemize
from pylatex.base_classes import LatexObject

from statements.intermidiaries.display.proposals.proposal import DisplayProposal
from statements.io.statement_compiler.latex.models.proposal import Proposal
from statements.io.statement_compiler.latex.sections.base_section import BaseSection


class Proposals(BaseSection):
    def __init__(self, proposals: list[DisplayProposal], **kwargs):
        self.proposals = proposals
        super().__init__(**kwargs)

    def make(self) -> LatexObject:
        proposal_list = Itemize()
        for proposal in self.proposals:
            proposal_list.add_item(Proposal(proposal))
        return proposal_list
