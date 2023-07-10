from pylatex.base_classes import LatexObject

class Break(LatexObject):
    def dumps(self):
        return r'\\'