
from statements.domain.progress_status import ProgressStatus
from statements.domain.statements.season_statement import SeasonStatement
from statements.intermidiaries.display.issue.adapter import IssueAdapter
from statements.intermidiaries.display.long_goals.adapter import LongGoalAdapter
from statements.intermidiaries.display.proposals.adapter import ProposalAdapter
from statements.intermidiaries.display.parts.season.status import DisplaySeasonStatus


class SeasonStatusAdapter:
    def __init__(self, goal_adapter: LongGoalAdapter, issue_adapter: IssueAdapter,
                 proposal_adapter: ProposalAdapter):
        self.goal_adapter = goal_adapter
        self.issue_adapter = issue_adapter
        self.proposal_adapter = proposal_adapter

    def get_display_status(self, statement: SeasonStatement) -> DisplaySeasonStatus:
        return DisplaySeasonStatus(
            goals=[self.goal_adapter.get_display_goal(goal, statement.projects_to_aspects)
                   for goal in statement.goals if goal.status in [ProgressStatus.TODO, ProgressStatus.IN_PROGRESS]],
            issues=[self.issue_adapter.get_display_issue(issue, statement.projects_to_aspects)
                    for issue in statement.issues],
            open_proposals=[self.proposal_adapter.get_display_proposal(proposal, statement.projects_to_aspects)
                            for proposal in statement.proposals
                            if proposal.accepted is None]
        )
