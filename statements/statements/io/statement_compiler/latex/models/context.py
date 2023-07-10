from statements.intermidiaries.display.context.context import DisplayContextItem
from statements.io.statement_compiler.latex.utils.insight import Insight


class ContextItem(Insight):
    def __init__(self, context_item: DisplayContextItem):
        super().__init__(context_item.project, context_item.description)