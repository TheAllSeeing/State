from pylatex.base_classes import LatexObject, Command
from pylatex.package import Package

from statements.intermidiaries.display.color.color import DisplayColor


class ColorDefinition(LatexObject):

    packages = [Package('xcolor')] 
    
    def __init__(self, color: DisplayColor):
        super().__init__()
        self.color = color
    
    def dumps(self):
        return Command('definecolor', arguments=[
            self.color.name, 'RGB', f'{self.color.red}, {self.color.green}, {self.color.blue}'
        ]).dumps()