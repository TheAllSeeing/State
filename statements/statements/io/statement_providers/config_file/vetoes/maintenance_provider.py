from abc import ABC

from statements.domain.vetoes.veto import Veto
from statements.domain.vetoes.veto_maintenance import VetoMaintenance, VetoViolation
from statements.io.statement_providers.config_file.vetoes.veto_maintenance import InputVetoMaintenance
from statements.io.statement_providers.config_file.toml_provider import TOMLProvider


class VetoMaintenanceProvider(ABC):
    def get_veto_maintenance(self, vetoes: dict[str, Veto]) -> list[VetoMaintenance]:
        pass


class TOMLVetoMaintenanceProvider(VetoMaintenanceProvider, TOMLProvider):
    def get_veto_maintenance(self, vetoes: dict[str, Veto]) -> list[VetoMaintenance]:
        raw_data = self._get_raw_data()
        parsed_data = InputVetoMaintenance.model_validate(raw_data).root
        return [VetoMaintenance(veto=vetoes[id_],
                                violations=[VetoViolation(date_=violation.date_, detail=violation.detail)
                                            for violation in violations])
                for id_, violations in parsed_data.items()]
