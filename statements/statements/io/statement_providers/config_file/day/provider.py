from abc import ABC, abstractmethod
from datetime import date, datetime, time

from pydantic import BaseModel

from statements.domain.day import Diary, Sleep, RestItem
from statements.io.statement_providers.config_file.day.day import InputDay
from statements.io.statement_providers.config_file.toml_provider import TOMLProvider


class Day(BaseModel):
    diary: Diary
    sleep: Sleep
    rest: list[RestItem]


class DayProvider(ABC):
    @abstractmethod
    def get_day(self, statement_date: date) -> Day:
        pass


class TOMLDayProvider(DayProvider, TOMLProvider):
    def get_day(self, statement_date: date) -> Day:
        raw_data = self._get_raw_data()
        input_day = InputDay.model_validate(raw_data)
        return Day(
            diary=Diary.model_validate({
                self.__get_full_date(time_, statement_date): description
                for time_, description in input_day.diary.root.items()
            }),
            sleep=Sleep(
                went=self.__get_full_date(input_day.sleep.went, statement_date),
                woke=self.__get_full_date(input_day.sleep.woke, statement_date),
                snooze=self.__get_full_date(input_day.sleep.snooze, statement_date),
            ),
            rest=[RestItem(title=title, description=item.description,
                           start=self.__get_full_date(item.start, statement_date),
                           end=self.__get_full_date(item.end, statement_date))
                  for title, item in input_day.rest.items()]
        )

    def __get_full_date(self, time_: datetime | time, statement_date: date) -> datetime:
        if isinstance(time_, datetime):
            return time_
        return datetime.combine(statement_date, time_)
