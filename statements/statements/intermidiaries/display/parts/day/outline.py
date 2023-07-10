from pydantic import BaseModel

from statements.intermidiaries.display.events.event import DisplayEvent
from statements.intermidiaries.display.tasks.task import DisplayTask
from statements.intermidiaries.display.vetoes.veto import DisplayVeto


class DisplayDayOutline(BaseModel):
    schedule: list[DisplayEvent]
    vetoes: list[DisplayVeto]
    tasks: list[DisplayTask]
    plan: list[DisplayEvent]
