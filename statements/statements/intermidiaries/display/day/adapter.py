from datetime import datetime

from datetime import date

from statements.domain.day import Sleep, Diary, RestItem
from statements.intermidiaries.display.day.day import DisplaySleep, DisplayDiary, DisplayRestItem


def _format_time(time: datetime, day: date):
    if time.date() == day:
        return time.strftime('%H:%M')
    else:
        return time.strftime(f'%H:%M')


class DiaryAdapter:
    def get_display_diary(self, diary: Diary, day: date) -> DisplayDiary:
        return DisplayDiary.model_validate(
            {_format_time(timepoint, day): description
             for timepoint, description in diary.root.items()}
        )


class SleepAdapter:
    def get_display_sleep(self, sleep: Sleep, day: date) -> DisplaySleep:
        snooze_minutes = (sleep.snooze - sleep.woke).seconds // 60
        return DisplaySleep(
            went=_format_time(sleep.went, day),
            woke=_format_time(sleep.woke, day),
            snooze=f'{_format_time(sleep.snooze, day)} ({snooze_minutes:02d} min)',
            slept=f'{sleep.slept.seconds // 3600:02d}:{sleep.slept.seconds % 3600 // 60:02d}',
        )


class RestAdapter:
    def get_display_rest_item(self, rest: RestItem) -> DisplayRestItem:
        total_time = (rest.end - rest.start).seconds
        return DisplayRestItem(
            time_range=f'{str(rest.start.time())[:-3]}-{str(rest.end.time())[:-3]}',
            title=rest.title,
            length=f'{total_time // 3600:02d}:{(total_time % 3600) // 60:02d}',
            description=rest.description
        )
