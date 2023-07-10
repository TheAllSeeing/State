from abc import ABC, abstractmethod

from statements.domain.statements.base_statement import Statement
from statements.domain.statements.season_statement import SeasonStatement


class StatementProvider(ABC):
    @abstractmethod
    def get_statement(self) -> Statement:
        pass
