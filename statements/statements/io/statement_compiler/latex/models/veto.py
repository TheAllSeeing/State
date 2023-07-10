from statements.intermidiaries.display.vetoes.veto import DisplayVeto
from statements.io.statement_compiler.latex.utils.insight import Insight


class Veto(Insight):
    def __init__(self, veto: DisplayVeto):
        super().__init__(project=veto.project, content=veto.description)