from pylatex import NoEscape

from statements.intermidiaries.display.settings.spacing_config import DisplaySpacingConfig
from statements.io.statement_compiler.latex.wrappers import SetLength
from statements.io.statement_compiler.latex.wrappers.bare_container import BareContainer


class Spacing(BareContainer):
    def __init__(self, config: DisplaySpacingConfig):
        super().__init__()
        self.append(SetLength([NoEscape(r'\parskip'), f'{config.paragraph_skip}em']))
        self.append(SetLength([NoEscape(r'\parindent'), f'{config.paragraph_indent}em']))
        self.append(NoEscape(r'\def\arraystretch{' + str(config.array_stretch) + r'}'))
