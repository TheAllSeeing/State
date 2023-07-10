import re

import mistletoe
from mistletoe.latex_renderer import LaTeXRenderer
from pylatex import Package
from pylatex.base_classes import LatexObject


class _DisplayFragmentRenderer(LaTeXRenderer):
    def render_link(self, token):
        self.packages['hyperref'] = []
        template = '\\href{{{inner}}}{{{target}}}'
        inner = self.render_inner(token)
        return template.format(target=token.target, inner=inner)

    def render_document(self, token):
        self.footnotes.update(token.footnotes)
        return self.render_inner(token)


class Markdown(LatexObject):
    packages = [Package('hyperref', options='unicode, colorlinks, bookmarks, bookmarksopen')]

    def __init__(self, content: str):
        super().__init__()
        self.content = re.sub(r'^[\t]+', '', content)

    def dumps(self):
        return mistletoe.markdown(self.content, _DisplayFragmentRenderer)

    def __bool__(self):
        return bool(self.content)


if __name__ == '__main__':
    with open('../../../../../../../src/outline/overview.md') as f:
        print(Markdown(f.read()).dumps())
