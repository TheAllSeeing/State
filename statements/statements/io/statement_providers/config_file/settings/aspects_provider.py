from abc import ABC, abstractmethod

from pydantic import parse_obj_as

from statements.domain.settings.aspect import Aspect
from statements.io.statement_providers.config_file.settings.aspect import InputAspect
from statements.io.statement_providers.config_file.toml_provider import TOMLProvider


class AspectsProvider(ABC):
    @abstractmethod
    def get_aspects(self) -> list[Aspect]:
        pass


class TOMLAspectsProvider(AspectsProvider, TOMLProvider):
    def get_aspects(self) -> list[Aspect]:
        raw_aspects = self._get_raw_data()
        input_aspects: dict[str, InputAspect] = parse_obj_as(dict[str, InputAspect], raw_aspects)
        return [Aspect(
            name=aspect_name,
            color=tuple(value*255 for value in aspect_data.rgb),
            active_projects=aspect_data.active_projects,
            passive_projects=aspect_data.passive_projects,
            frozen_projects=aspect_data.frozen_projects,
            archived_projects=aspect_data.archived_projects,
        ) for aspect_name, aspect_data in input_aspects.items()]
