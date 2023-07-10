from statements.domain.statements.season_statement import SeasonStatement
from statements.intermidiaries.display.events.adapter import EventAdapter
from statements.intermidiaries.display.habits.adapter import HabitAdapter
from statements.intermidiaries.display.long_goals.adapter import LongGoalAdapter
from statements.intermidiaries.display.vetoes.adapter import VetoAdapter
from statements.intermidiaries.display.parts.season.outline import DisplaySeasonOutline


class SeasonOutlineAdapter:
    def __init__(self, goal_adapter: LongGoalAdapter, event_adapter: EventAdapter,
                 habit_adapter: HabitAdapter, veto_adapter: VetoAdapter):
        self.goal_adapter = goal_adapter
        self.event_adapter = event_adapter
        self.habit_adapter = habit_adapter
        self.veto_adapter = veto_adapter

    def get_display_outline(self, statement: SeasonStatement) -> DisplaySeasonOutline:
        return DisplaySeasonOutline(
            overview=statement.overview,
            schedule=[self.event_adapter.get_display_event(event, statement.projects_to_aspects) for event in
                      statement.schedule],
            goals=[self.goal_adapter.get_display_goal(goal, statement.projects_to_aspects) for goal in statement.goals],
            habits=[self.habit_adapter.get_display_habit(habit, statement.projects_to_aspects) for habit in
                    statement.habits],
            vetoes=[self.veto_adapter.get_display_veto(veto, statement.projects_to_aspects) for veto in
                    statement.vetoes],
            plan=[self.event_adapter.get_display_event(event, statement.projects_to_aspects) for event in
                  statement.timeline]
        )
