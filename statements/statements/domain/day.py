from datetime import datetime

from datetime import timedelta
from pydantic import RootModel, BaseModel

Diary = RootModel[dict[datetime, str]]


class Sleep(BaseModel):
    went: datetime
    woke: datetime
    snooze: datetime

    @property
    def slept(self) -> timedelta:
        return self.snooze - self.went


class RestItem(BaseModel):
    title: str
    start: datetime
    end: datetime
    description: str
