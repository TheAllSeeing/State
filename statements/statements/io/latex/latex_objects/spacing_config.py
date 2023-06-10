from pylatex import NoEscape

from statements.io.latex.models.spacing_config import LatexSpacingConfig
from statements.io.latex.utils import SetLength
from statements.io.latex.utils.bare_container import BareContainer


class Spacing(BareContainer):
    def __init__(self, config: LatexSpacingConfig):
        super().__init__()
        self.append(SetLength([NoEscape(r'\parskip'), f'{config.paragraph_skip}em']))
        self.append(SetLength([NoEscape(r'\parindent'), f'{config.paragraph_indent}em']))
        self.append(NoEscape(r'\def\arraystretch{' + str(config.array_stretch) + r'}'))
