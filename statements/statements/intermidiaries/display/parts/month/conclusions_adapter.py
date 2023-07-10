from statements.domain.statements.month_statement import MonthlyStatement
from statements.intermidiaries.display.goals.adapter import GoalAdapter
from statements.intermidiaries.display.goals.closure_adapter import GoalClosureAdapter
from statements.intermidiaries.display.parts.month.conclusions import DisplayMonthConclusions
from statements.intermidiaries.display.proposals.adapter import ProposalAdapter


class MonthConclusionsAdapter:
    def __init__(self, goal_adapter: GoalAdapter, goal_closure_adapter: GoalClosureAdapter,
                 proposal_adapter: ProposalAdapter):
        self.goal_adapter = goal_adapter
        self.goal_closure_adapter = goal_closure_adapter
        self.proposal_adapter = proposal_adapter

    def get_display_conclusions(self, statement: MonthlyStatement) -> DisplayMonthConclusions:
        return DisplayMonthConclusions(
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
