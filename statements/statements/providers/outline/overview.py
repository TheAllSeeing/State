from abc import ABC, abstractmethod
from pathlib import Path

from statements.domain.outline.outline import Markdown


class OverviewProvider(ABC):
    @abstractmethod
    def get_overview(self) -> Markdown:
        pass


class FileOverviewProvider(OverviewProvider):
    def __init__(self, file_path: Path):
        self.file_path = file_path

    def get_overview(self) -> Markdown:
        with open(self.file_path, 'r') as overview_file:
            return overview_file.read()
