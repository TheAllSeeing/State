from statements.domain.progress_status import ProgressStatus
from statements.io.statement_providers.config_file.progress_status.progress_status import InputProgressStatus


class InputProgressStatusAdapter:

    def get_progress_status(self, input_status: InputProgressStatus) -> ProgressStatus:
        return getattr(ProgressStatus, input_status.name)
