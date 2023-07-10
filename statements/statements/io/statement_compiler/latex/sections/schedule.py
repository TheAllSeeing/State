from pylatex.base_classes import LatexObject

from statements.intermidiaries.display.events.event import DisplayEvent
from statements.io.statement_compiler.latex.models.timeline import Timeline
from statements.io.statement_compiler.latex.sections.base_section import BaseSection


class Schedule(BaseSection):
    def __init__(self, events: list[DisplayEvent]):
        self.events = events
        super().__init__()

    def make(self) -> LatexObject | None:
        timeline = Timeline(color='Steel')
        for event in self.events:
            timeline.append(event)
        return timeline
