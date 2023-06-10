import tomllib
from abc import ABC, abstractmethod
from pathlib import Path

from statements.domain.outline.event import Event


class TimelineProvider(ABC):
    @abstractmethod
    def get_timeline(self) -> list[Event]:
        pass


class TOMLTimelineProvider(TimelineProvider):
    def __init__(self, file_path: Path):
        self.file_path = file_path

    def get_timeline(self) -> list[Event]:
        with open(self.file_path, 'rb') as timeline_file:
            raw_timeline = tomllib.load(timeline_file)

        return [
            Event(
                time=time,
                project=project,
                description=description
            ) for time, projects in raw_timeline.items()
            for project, project_events in projects.items()
            for description in project_events
        ]
