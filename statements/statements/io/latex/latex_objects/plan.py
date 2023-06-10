from statements.io.latex.latex_objects.timeline import Timeline
from statements.io.latex.models.event import LatexEvent


class Schedule(Timeline):
    def __init__(self, events: list[LatexEvent]):
        super().__init__()
        for event in events:
            self.append(event)