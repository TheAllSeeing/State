from pylatex.base_classes import Command

from statements.intermidiaries.display.settings.color_config import DisplayColorConfig
from statements.io.statement_compiler.latex.wrappers.bare_container import BareContainer
from statements.io.statement_compiler.latex.utils.color_definition import ColorDefinition


class ColorConfig(BareContainer):
    content_separator = '\n'
    def __init__(self, color_config: DisplayColorConfig):
        super().__init__()
        self.append(ColorDefinition(color_config.page_color))
        self.append(ColorDefinition(color_config.text_color))
        self.append(ColorDefinition(color_config.link_color))
        self.append(Command('pagecolor', color_config.page_color.name))
        self.append(Command('color', color_config.text_color.name))
        self.append(Command('hypersetup', f'urlcolor={color_config.link_color.name}'))
