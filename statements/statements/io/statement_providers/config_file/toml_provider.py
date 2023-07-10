import tomllib
from pathlib import Path


class TOMLProvider:
    def __init__(self, file_path: Path):
        self.file_path = file_path

    def _get_raw_data(self):
        with open(self.file_path, 'rb') as f:
            return tomllib.load(f)
