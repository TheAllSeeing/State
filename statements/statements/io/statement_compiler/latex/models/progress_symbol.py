from pylatex import Package, NoEscape
from pylatex.base_classes.containers import Fragment

from statements.consts import RESOURCES_DIR
from statements.intermidiaries.display.progress_status.progress_status import DisplayProgressStatus
from statements.io.statement_compiler.latex.wrappers import Phantom, Tiny
from statements.io.statement_compiler.latex.wrappers.encircle import Encircle
from statements.io.statement_compiler.latex.utils.checkmark import Checkmark

STATUS_TO_SYMBOL = {
    DisplayProgressStatus.TODO: Phantom('x'),
    DisplayProgressStatus.IN_PROGRESS: Tiny(Encircle(Phantom('x'))),
    DisplayProgressStatus.DONE: Tiny(Checkmark()),
    DisplayProgressStatus.FAILED: 'x'
}


class ProgressSymbol(Fragment):
    packages = [Package('amssymb'), Package(NoEscape(f'{RESOURCES_DIR}/encircle'))]

    def __init__(self, status: DisplayProgressStatus):
        super().__init__()
        self.append(Encircle(STATUS_TO_SYMBOL[status]))
