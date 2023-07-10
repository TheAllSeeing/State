from pylatex import Package, NoEscape
from pylatex.base_classes import CommandBase

from statements.consts import RESOURCES_DIR


class Encircle(CommandBase):
    packages = [Package(NoEscape(f'{RESOURCES_DIR}/encircle'))]
