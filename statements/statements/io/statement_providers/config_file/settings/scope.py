from datetime import date
from enum import Enum

from pydantic import BaseModel, Field


class InputStatementType(str, Enum):
    DAY = 'Day'
    WEEK = 'Week'
    MONTH = 'Month'
    SEASON = 'Season'


class InputScope(BaseModel):
    type_: InputStatementType = Field(alias='type')
    start: date
