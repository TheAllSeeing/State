import re
from abc import ABC, abstractmethod

from pylatex import Section
from pylatex.base_classes import LatexObject

from statements.io.statement_compiler.latex.wrappers import MedSkip


def _class_name_to_title(class_name: str):
    return re.sub(r'(?<!^)(?=[A-Z])', ' ', class_name)


class BaseSection(Section, ABC):
    _latex_name = Section.__name__.lower()
    _title = None

    def __init__(self, title: str = None):
        super().__init__(_class_name_to_title(title or self._title or self.__class__.__name__))
        content = self.make()
        if content:
            self.append(MedSkip())
            self.append(content)
        else:
            self.append('N/A')

    @abstractmethod
    def make(self) -> LatexObject:
        pass
