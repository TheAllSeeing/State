from pydantic import BaseModel, RootModel

from statements.intermidiaries.display.validation_types import TimeString, Description, TimeRangeString

DisplayDiary = RootModel[dict[TimeString, Description]]


class DisplaySleep(BaseModel):
    went: TimeString
    woke: TimeString
    snooze: TimeString
    slept: TimeString


class DisplayRestItem(BaseModel):
    title: str
    time_range: TimeRangeString
    length: TimeString
    description: str


DisplayRest = RootModel[list[DisplayRestItem]]

