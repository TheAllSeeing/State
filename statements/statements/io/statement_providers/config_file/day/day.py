from datetime import time, datetime

from pydantic import RootModel, BaseModel, Field

from statements.io.statement_providers.config_file.validation_types import Title

InputDiary = RootModel[dict[time | datetime, str]]


class InputSleep(BaseModel):
    went: time | datetime
    woke: time | datetime
    snooze: time | datetime


class InputRestItem(BaseModel):
    start: time | datetime
    end: time | datetime
    description: str


class InputDay(BaseModel):
    diary: InputDiary = Field(alias='Diary')
    sleep: InputSleep = Field(alias='Sleep')
    rest: dict[Title, InputRestItem] = Field(alias='Rest')
