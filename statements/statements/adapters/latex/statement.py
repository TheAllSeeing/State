from statements.adapters.latex.aspect import AspectAdapter
from statements.adapters.latex.outline import OutlineAdapter
from statements.adapters.latex.settings import TitleConfigAdapter
from statements.domain.statement import Statement
from statements.io.latex.statement import Statement as LatexStatement


class StatementAdapter:
    def __init__(self, aspects_adapter: AspectAdapter, outline_adapter: OutlineAdapter,
                 title_adapter: TitleConfigAdapter):
        self.aspects_adapter = aspects_adapter
        self.outline_adapter = outline_adapter
        self.title_adapter = title_adapter

    def get_latex_statement(self, statement: Statement):
        return LatexStatement(
            aspects=[self.aspects_adapter.get_latex_aspect(aspect) for aspect in statement.aspects],
            title_config=self.title_adapter.get_latex_title_config(statement.config.title),
            outline=self.outline_adapter.get_latex_outline(statement.outline)
        )
