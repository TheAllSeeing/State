from datetime import date
from enum import Enum

from datetime import timedelta
from pydantic import BaseModel


class StatementType(str, Enum):
    DAY = 'day'
    WEEK = 'week'
    MONTH = 'month'
    SEASON = 'season'


class StatementScope(BaseModel):
    type_: StatementType
    start: date

    @property
    def end(self) -> date:
        match self.type_:
            case StatementType.DAY:
                return self.start
            case StatementType.WEEK:
                return self.start + timedelta(days=6)
            case StatementType.MONTH:
                return self.start.replace(month=self.start.month + 1)
            case StatementType.SEASON:
                return self.start.replace(month=self.start.month + 3)
            case _:
                raise NotImplementedError(f'Unsupported statement type: {self.type_.value}')
