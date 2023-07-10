from enum import Enum


class InputProgressStatus(Enum):
    TODO = 'O'
    IN_PROGRESS = 'D'
    DONE = 'V'
    FAILED = 'X'
