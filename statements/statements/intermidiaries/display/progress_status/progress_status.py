from enum import Enum


class DisplayProgressStatus(Enum):
    TODO = 'To do'
    DONE = 'Done'
    FAILED = 'Failed'
    IN_PROGRESS = 'In Progress'
