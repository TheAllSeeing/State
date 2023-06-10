import pandoc
from pylatex import Package
from pylatex.base_classes import LatexObject

pandoc.configure(path='/usr/bin/pandoc', pandoc_types_version='1.23')


class Markdown(LatexObject):
    packages = [Package('hyperref')]

    def __init__(self, content: str):
        super().__init__()
        self.content = content

    def dumps(self):
        pandoc_document = pandoc.read(self.content, format='markdown')
        return pandoc.write(pandoc_document, format='latex')


if __name__ == '__main__':
    with open('../../../../../src/outline/overview.md') as f:
        print(Markdown(f.read()).dumps())
