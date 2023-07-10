from datetime import date

from pydantic import BaseModel

from statements.domain.vetoes.veto import Veto


class VetoViolation(BaseModel):
    date_: date
    detail: str


class VetoMaintenance(BaseModel):
    veto: Veto
    violations: list[VetoViolation]

