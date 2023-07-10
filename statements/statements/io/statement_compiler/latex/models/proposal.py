from pylatex.base_classes.containers import Fragment
from pylatex.utils import bold

from statements.intermidiaries.display.proposals.proposal import DisplayProposal
from statements.io.statement_compiler.latex.utils.insight import Insight


class Proposal(Insight):
    def __init__(self, proposal: DisplayProposal):
        content = Fragment()
        content.append(proposal.description)

        if proposal.status:
            content.append(' | ')
            content.append(bold(proposal.status.value.upper()))

        super().__init__(project=proposal.project, content=content)