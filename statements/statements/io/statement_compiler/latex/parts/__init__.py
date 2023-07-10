import re

from pylatex.section import Part


def _class_name_to_title(class_name: str):
    return ' '.join(re.split(r'(?<!^)(?=[A-Z])', class_name)[1:])


class BasePart(Part):
    _latex_name = 'part'

    def __init__(self, **kwargs):
        super().__init__(_class_name_to_title(self.__class__.__name__), **kwargs)
