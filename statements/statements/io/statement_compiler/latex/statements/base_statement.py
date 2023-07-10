import itertools

from pylatex import Document, Command, Package, NoEscape, NewPage

from statements.intermidiaries.display.statements.base_statement import DisplayStatement
from statements.io.statement_compiler.latex.models.color_config import ColorConfig
from statements.io.statement_compiler.latex.models.project_block import ProjectBlock
from statements.io.statement_compiler.latex.models.spacing_config import Spacing
from statements.io.statement_compiler.latex.utils.color_definition import ColorDefinition
from statements.io.statement_compiler.latex.wrappers.new_paragraph import NewParagraph
from statements.io.statement_compiler.latex.wrappers.skip import Skip

TITLE_PROJECT_SKIP_COUNT = 3


class BaseStatement(Document):
    def __init__(self, statement_model: DisplayStatement, **kwargs):
        super().__init__(**kwargs)

        self.packages.append(Package(statement_model.style.font_config.font_family))
        self.preamble.append(Spacing(statement_model.style.spacing_config))
        self.preamble.append(ColorConfig(statement_model.style.color_config))

        for aspect in statement_model.aspects:
            self.preamble.append(ColorDefinition(aspect.color))

        self.preamble.append(Command('title', statement_model.title_config.title))
        self.preamble.append(Command('author', statement_model.title_config.themes))
        self.preamble.append(Command('date', NoEscape(statement_model.title_config.scope)))
        self.append(Command('maketitle'))
        self.append(Skip(TITLE_PROJECT_SKIP_COUNT))

        active_projects = list(itertools.chain(
            *[aspect.active_projects for aspect in statement_model.aspects]))
        passive_projects = list(itertools.chain(
            *[aspect.passive_projects for aspect in statement_model.aspects]))

        self.append(ProjectBlock(projects=active_projects, active=True))
        self.append(NewParagraph())
        self.append(ProjectBlock(projects=passive_projects, active=False))

        self.append(NewPage())
