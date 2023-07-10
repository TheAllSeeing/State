from pylatex.base_classes import LatexObject

class NewParagraph(LatexObject):
    def dumps(self):
        return '\n\n'