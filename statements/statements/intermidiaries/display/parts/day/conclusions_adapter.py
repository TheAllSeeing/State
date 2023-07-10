from statements.domain.statements.day_statement import DailyStatement
from statements.intermidiaries.display.goals.adapter import GoalAdapter
from statements.intermidiaries.display.goals.closure_adapter import GoalClosureAdapter
from statements.intermidiaries.display.parts.day.conclusions import DisplayDayConclusions
from statements.intermidiaries.display.proposals.adapter import ProposalAdapter
from statements.intermidiaries.display.tasks.adapter import TaskAdapter


class DayConclusionsAdapter:
    def __init__(self, task_adapter: TaskAdapter, proposal_adapter: ProposalAdapter):
        self.task_adapter = task_adapter
        self.proposal_adapter = proposal_adapter

    def get_display_conclusions(self, statement: DailyStatement) -> DisplayDayConclusions:
        return DisplayDayConclusions(
            new_tasks=[self.task_adapter.get_display_task(task, statement.projects_to_aspects)
                       for task in statement.new_tasks],
            new_proposals=[self.proposal_adapter.get_display_proposal(proposal, statement.projects_to_aspects)
                           for proposal in statement.new_proposals],
            notes=statement.notes
        )
