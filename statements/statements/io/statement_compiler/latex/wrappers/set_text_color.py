from pylatex import Package
from pylatex.base_classes import CommandBase


class SetTextColor(CommandBase):
    _latex_name = 'color'
    packages = [Package('xcolor')]
