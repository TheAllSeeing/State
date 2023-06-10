from statements.domain.outline.outline import Outline
from statements.providers.outline.overview import OverviewProvider
from statements.providers.outline.long_goals import LongGoalProvider
from statements.providers.outline.timeline import TimelineProvider


class OutlineProvider:
    def __init__(self, overview_provider: OverviewProvider, schedule_provider: TimelineProvider, goals_provider: LongGoalProvider):
        self.overview_provider = overview_provider
        self.goals_provider = goals_provider
        self.schedule_provider = schedule_provider

    def get_outline(self):
        return Outline(
            overview=self.overview_provider.get_overview(),
            schedule=self.schedule_provider.get_timeline(),
            goals=self.goals_provider.get_long_goals()
        )
