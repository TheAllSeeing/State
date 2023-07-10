from enum import Enum


class ProgressStatus(Enum):
    TODO = 'To do'
    DONE = 'Done'
    FAILED = 'Failed'
    IN_PROGRESS = 'In Progress'
