from abc import ABC, abstractmethod

from statements.domain.events.event import Event
from statements.io.statement_providers.config_file.toml_provider import TOMLProvider


class TimelineProvider(ABC):
    @abstractmethod
    def get_timeline(self) -> list[Event]:
        pass


class TOMLTimelineProvider(TimelineProvider, TOMLProvider):
    def get_timeline(self) -> list[Event]:
        raw_timeline = self._get_raw_data()
        return [
            Event(
                time=time,
                project=project,
                description=description
            ) for time, projects in raw_timeline.items()
            for project, project_events in projects.items()
            for description in project_events
        ]
