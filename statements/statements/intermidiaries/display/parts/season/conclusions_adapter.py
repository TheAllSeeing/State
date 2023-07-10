from statements.domain.statements.season_statement import SeasonStatement
from statements.intermidiaries.display.long_goals.closure_adapter import LongGoalClosureAdapter
from statements.intermidiaries.display.long_goals.adapter import LongGoalAdapter
from statements.intermidiaries.display.projects.status_change_adapter import ProjectStatusChangeAdapter
from statements.intermidiaries.display.parts.season.conclusions import DisplaySeasonConclusions
from statements.intermidiaries.display.proposals.adapter import ProposalAdapter


class SeasonConclusionsAdapter:
    def __init__(self, project_status_change_adapter: ProjectStatusChangeAdapter,
                 goal_adapter: LongGoalAdapter, goal_closure_adapter: LongGoalClosureAdapter,
                 proposal_adapter: ProposalAdapter):
        self.project_status_change_adapter = project_status_change_adapter
        self.goal_adapter = goal_adapter
        self.goal_closure_adapter = goal_closure_adapter
        self.proposal_adapter = proposal_adapter

    def get_display_conclusions(self, statement: SeasonStatement) -> DisplaySeasonConclusions:
        return DisplaySeasonConclusions(
            project_status_changes=self.project_status_change_adapter.get_display_status_changes(
                statement.project_status_changes, statement.projects_to_aspects
            ),
            new_goals=[self.goal_adapter.get_display_goal(goal, statement.projects_to_aspects)
                       for goal in statement.new_goals],
            closed_goals=[
                self.goal_closure_adapter.get_display_goal_closure(goal_closure, statement.projects_to_aspects)
                for goal_closure in statement.goal_closures
            ],
            new_proposals=[self.proposal_adapter.get_display_proposal(proposal, statement.projects_to_aspects)
                           for proposal in statement.new_proposals],
            notes=statement.notes
        )
