from statements.domain.settings.aspect import Aspect
from statements.domain.events.event import Event
from statements.intermidiaries.display.projects.adapter import ProjectAdapter
from statements.intermidiaries.display.events.event import DisplayEvent


class EventAdapter:
    def __init__(self, project_adapter: ProjectAdapter):
        self.project_adapter = project_adapter

    def get_display_event(self, event: Event, projects: dict[str, Aspect]) -> DisplayEvent:
        return DisplayEvent(
            time=event.time,
            project=self.project_adapter.get_display_project(event.project, projects),
            description=event.description
        )
