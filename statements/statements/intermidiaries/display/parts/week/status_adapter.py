
from statements.domain.progress_status import ProgressStatus
from statements.domain.statements.week_statement import WeeklyStatement
from statements.intermidiaries.display.issue.adapter import IssueAdapter
from statements.intermidiaries.display.goals.adapter import GoalAdapter
from statements.intermidiaries.display.proposals.adapter import ProposalAdapter
from statements.intermidiaries.display.parts.week.status import DisplayWeekStatus
from statements.intermidiaries.display.tasks.adapter import TaskAdapter


class WeekStatusAdapter:
    def __init__(self, goal_adapter: GoalAdapter, issue_adapter: IssueAdapter,
                 task_adapter: TaskAdapter, proposal_adapter: ProposalAdapter):
        self.goal_adapter = goal_adapter
        self.issue_adapter = issue_adapter
        self.task_adapter = task_adapter
        self.proposal_adapter = proposal_adapter

    def get_display_status(self, statement: WeeklyStatement) -> DisplayWeekStatus:
        return DisplayWeekStatus(
            goals=[self.goal_adapter.get_display_goal(goal, statement.projects_to_aspects)
                   for goal in statement.goals if goal.status in [ProgressStatus.TODO, ProgressStatus.IN_PROGRESS]],
            issues=[self.issue_adapter.get_display_issue(issue, statement.projects_to_aspects)
                    for issue in statement.issues],
            open_tasks=[self.task_adapter.get_display_task(task, statement.projects_to_aspects)
                        for task in statement.tasks if task.status in [ProgressStatus.TODO, ProgressStatus.IN_PROGRESS]],
            open_proposals=[self.proposal_adapter.get_display_proposal(proposal, statement.projects_to_aspects)
                            for proposal in statement.proposals
                            if proposal.accepted is None]
        )
