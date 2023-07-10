from pylatex import Package
from pylatex.base_classes import CommandBase


class Underline(CommandBase):
    _latex_name = 'uline'
    packages = [Package('ulem', options='normalem')]
