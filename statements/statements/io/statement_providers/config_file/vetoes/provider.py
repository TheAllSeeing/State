from abc import ABC, abstractmethod

from statements.domain.vetoes.veto import Veto
from statements.io.statement_providers.config_file.vetoes.veto import InputVetoes
from statements.io.statement_providers.config_file.toml_provider import TOMLProvider


class VetoesProvider(ABC):
    @abstractmethod
    def get_vetoes(self) -> list[Veto]:
        pass


class TOMLVetoesProvider(VetoesProvider, TOMLProvider):
    def get_vetoes(self) -> list[Veto]:
        raw_vetoes = self._get_raw_data()
        parsed_vetoes = InputVetoes.model_validate(raw_vetoes).root
        return [
            Veto(id_=veto_data.id_, project=project, description=veto_data.description)
            for project, project_vetoes in parsed_vetoes.items()
            for veto_data in project_vetoes
        ]
