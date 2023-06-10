from pylatex.base_classes import Command

from statements.io.latex.latex_objects.color_definition import ColorDefinition
from statements.io.latex.models.color_config import LatexColorConfig
from statements.io.latex.utils.bare_container import BareContainer


class ColorConfig(BareContainer):
    def __init__(self, color_config: LatexColorConfig):
        super().__init__()
        self.append(ColorDefinition(color_config.page_color))
        self.append(ColorDefinition(color_config.text_color))
        self.append(Command('pagecolor', color_config.page_color.name))
        self.append(Command('color', color_config.text_color.name))
