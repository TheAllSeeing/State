
from statements.domain.progress_status import ProgressStatus
from statements.domain.statements.month_statement import MonthlyStatement
from statements.intermidiaries.display.issue.adapter import IssueAdapter
from statements.intermidiaries.display.goals.adapter import GoalAdapter
from statements.intermidiaries.display.proposals.adapter import ProposalAdapter
from statements.intermidiaries.display.parts.month.status import DisplayMonthStatus


class MonthStatusAdapter:
    def __init__(self, goal_adapter: GoalAdapter, issue_adapter: IssueAdapter,
                 proposal_adapter: ProposalAdapter):
        self.goal_adapter = goal_adapter
        self.issue_adapter = issue_adapter
        self.proposal_adapter = proposal_adapter

    def get_display_status(self, statement: MonthlyStatement) -> DisplayMonthStatus:
        return DisplayMonthStatus(
            goals=[self.goal_adapter.get_display_goal(goal, statement.projects_to_aspects)
                   for goal in statement.goals if goal.status in [ProgressStatus.TODO, ProgressStatus.IN_PROGRESS]],
            issues=[self.issue_adapter.get_display_issue(issue, statement.projects_to_aspects)
                    for issue in statement.issues],
            open_proposals=[self.proposal_adapter.get_display_proposal(proposal, statement.projects_to_aspects)
                            for proposal in statement.proposals
                            if proposal.accepted is None]
        )
