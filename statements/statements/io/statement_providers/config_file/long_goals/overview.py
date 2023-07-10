from abc import ABC, abstractmethod
from pathlib import Path

from statements.domain.validation_types import Markdown


class MarkdownProvider(ABC):
    @abstractmethod
    def get_markdown(self) -> Markdown:
        pass


class FileMarkdownProvider(MarkdownProvider):
    def __init__(self, file_path: Path):
        self.file_path = file_path

    def get_markdown(self) -> Markdown:
        with open(self.file_path, 'r') as overview_file:
            return overview_file.read()
