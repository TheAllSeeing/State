from pylatex.base_classes import Container, LatexObject

class Group(Container):
    def __init__(self):
        super().__init__(data=[])

    def append(self, item):
        if not isinstance(item, (str, LatexObject)):
            raise TypeError('Group items must be strings or LatexObjects')
        return super().append(item)

    def dumps(self):
        latex_atoms = [
            atom.dumps() if isinstance(atom, LatexObject) else atom
            for atom in self.data
        ]
        return '{\n\t' + '\n\t'.join(' '.join(latex_atoms).splitlines()) + '\n}'
