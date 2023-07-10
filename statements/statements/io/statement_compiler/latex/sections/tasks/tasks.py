from pylatex import Itemize
from pylatex.base_classes import LatexObject

from statements.intermidiaries.display.tasks.task import DisplayTask
from statements.io.statement_compiler.latex.models.task import Task
from statements.io.statement_compiler.latex.sections.base_section import BaseSection


class Tasks(BaseSection):
    def __init__(self, tasks_statuses: list[DisplayTask]):
        self.task_statuses = tasks_statuses
        super().__init__()

    def make(self) -> LatexObject:
        status_list = Itemize()
        for task_status in self.task_statuses:
            status_list.add_item(Task(task_status))
        return status_list
