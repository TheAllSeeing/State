from statements.domain.progress_status import ProgressStatus
from statements.intermidiaries.display.progress_status.progress_status import DisplayProgressStatus

DOMAIN_TO_DISPLAY_STATUS = {
    ProgressStatus.TODO: DisplayProgressStatus.TODO,
    ProgressStatus.IN_PROGRESS: DisplayProgressStatus.IN_PROGRESS,
    ProgressStatus.DONE: DisplayProgressStatus.DONE,
    ProgressStatus.FAILED: DisplayProgressStatus.FAILED
}


class ProgressStatusAdapter:
    def get_progress_status(self, progress_status: ProgressStatus) -> DisplayProgressStatus:
        return DOMAIN_TO_DISPLAY_STATUS[progress_status]
