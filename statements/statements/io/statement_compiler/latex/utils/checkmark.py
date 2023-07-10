from pylatex import Package
from pylatex.base_classes import CommandBase


class Checkmark(CommandBase):
    packages = [Package('amssymb')]