from pylatex.base_classes import LatexObject, Container


class BareContainer(Container):
    content_separator = ' '

    def append(self, item):
        if not isinstance(item, (str, LatexObject)):
            raise TypeError('Group items must be strings or LatexObjects')
        return super().append(item)

    def dumps(self):
        return self.dumps_content()
