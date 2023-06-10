import tomllib
from abc import ABC, abstractmethod
from pathlib import Path

from pydantic import parse_obj_as

from statements.io.config.aspect import InputAspect
from statements.domain.settings.aspect import Aspect


class AspectsProvider(ABC):
    @abstractmethod
    def get_aspects(self) -> list[Aspect]:
        pass


class TOMLAspectsProvider(AspectsProvider):
    def __init__(self, file_path: Path):
        self.file_path = file_path

    def get_aspects(self) -> list[Aspect]:
        with open(self.file_path, 'rb') as aspects_file:
            raw_aspects = tomllib.load(aspects_file)
        input_aspects: dict[str, InputAspect] = parse_obj_as(dict[str, InputAspect], raw_aspects)
        return [Aspect(
            name=aspect_name,
            color=tuple(value*255 for value in aspect_data.rgb),
            active_projects=aspect_data.active_projects,
            passive_projects=aspect_data.passive_projects,
            frozen_projects=aspect_data.frozen_projects,
            archived_projects=aspect_data.archived_projects,
        ) for aspect_name, aspect_data in input_aspects.items()]
