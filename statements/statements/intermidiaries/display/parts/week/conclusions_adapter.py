from statements.domain.statements.week_statement import WeeklyStatement
from statements.intermidiaries.display.goals.adapter import GoalAdapter
from statements.intermidiaries.display.goals.closure_adapter import GoalClosureAdapter
from statements.intermidiaries.display.parts.week.conclusions import DisplayWeekConclusions
from statements.intermidiaries.display.proposals.adapter import ProposalAdapter
from statements.intermidiaries.display.tasks.adapter import TaskAdapter


class WeekConclusionsAdapter:
    def __init__(self, goal_adapter: GoalAdapter, task_adapter: TaskAdapter,
                 proposal_adapter: ProposalAdapter):
        self.goal_adapter = goal_adapter
        self.task_adapter = task_adapter
        self.proposal_adapter = proposal_adapter

    def get_display_conclusions(self, statement: WeeklyStatement) -> DisplayWeekConclusions:
        return DisplayWeekConclusions(
            new_goals=[self.goal_adapter.get_display_goal(goal, statement.projects_to_aspects)
                       for goal in statement.new_goals],
            new_tasks=[self.task_adapter.get_display_task(task, statement.projects_to_aspects)
                       for task in statement.new_tasks],
            new_proposals=[self.proposal_adapter.get_display_proposal(proposal, statement.projects_to_aspects)
                           for proposal in statement.new_proposals],
            notes = statement.notes
        )
