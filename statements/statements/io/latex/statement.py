import itertools
from typing import Self

from pylatex import Document, Command, Package, NewPage, NoEscape

from statements.io.latex.defaults import DEFAULT_STYLE
from statements.io.latex.latex_objects.color_config import ColorConfig
from statements.io.latex.latex_objects.color_definition import ColorDefinition
from statements.io.latex.latex_objects.project_block import ProjectBlock
from statements.io.latex.latex_objects.spacing_config import Spacing
from statements.io.latex.models.style import StatementStyle
from statements.io.latex.models.aspect import LatexAspect
from statements.io.latex.models.color import LatexColor
from statements.io.latex.models.outline import LatexOutline
from statements.io.latex.models.title_config import LatexTitleConfig
from statements.io.latex.sections.outline import Outline
from statements.io.latex.utils.new_paragraph import NewParagraph
from statements.io.latex.utils.skip import Skip

TITLE_PROJECT_SKIP_COUNT = 3


class Statement(Document):
    def __init__(self, *,
                 aspects: list[LatexAspect],
                 title_config: LatexTitleConfig,
                 outline: LatexOutline,
                 statement_style: StatementStyle = DEFAULT_STYLE,
                 **kwargs
                 ):
        super().__init__(**kwargs)
        self.aspects = aspects
        self.title_config = title_config
        self.style = statement_style

        self.outline = outline

    def build(self) -> Self:
        self.packages.append(Package(self.style.font_config.font_family))
        self.preamble.append(Spacing(self.style.spacing_config))
        self.preamble.append(ColorConfig(self.style.color_config))

        for aspect in self.aspects:
            self.preamble.append(ColorDefinition(aspect.color))

        self.preamble.append(Command('title', self.title_config.title))
        self.preamble.append(Command('author', self.title_config.themes))
        self.preamble.append(Command('date', NoEscape(self.title_config.scope)))
        self.append(Command('maketitle'))
        self.append(Skip(TITLE_PROJECT_SKIP_COUNT))

        active_projects = list(itertools.chain(
            *[aspect.active_projects for aspect in self.aspects]))
        passive_projects = list(itertools.chain(
            *[aspect.passive_projects for aspect in self.aspects]))

        self.append(ProjectBlock(projects=active_projects, active=True))
        self.append(NewParagraph())
        self.append(ProjectBlock(projects=passive_projects, active=False))

        self.append(NewPage())
        self.append(Outline(self.outline))

        return self


if __name__ == '__main__':
    from statements.io.latex.models.project import LatexProject

    title_config = LatexTitleConfig(
        title='Test',
        theme='Clarity | Test',
        scope='today'
    )

    steel = LatexColor(name='steel', red=0.75, green=0.75, blue=0.75)
    blue = LatexColor(name='blue', red=0.04, green=0.04, blue=0.47)

    aspects = [
        LatexAspect(
            name='Steel',
            color=steel,
            active_projects=[LatexProject(name='CONTROL', color=steel)] * 2,
            passive_projects=[],
            frozen_projects=[],
            archived_projects=[]
        ),

        LatexAspect(
            name='Blue',
            color=blue,
            active_projects=[LatexProject(name='SOMETHING', color=blue)] * 4,
            passive_projects=[LatexProject(name='VEGAN', color=blue)],
            frozen_projects=[],
            archived_projects=[]
        )
    ]

    doc = Statement(
        title_config=title_config,
        aspects=aspects
    )
    doc.build()
    doc.generate_pdf('Statement', compiler='lualatex', clean_tex=False)
