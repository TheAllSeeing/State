from pylatex import Itemize
from pylatex.base_classes import LatexObject

from statements.intermidiaries.display.tasks.task import DisplayTask
from statements.io.statement_compiler.latex.models.task import OutlineTask
from statements.io.statement_compiler.latex.sections.base_section import BaseSection


class StatuslessTasks(BaseSection):
    def __init__(self, tasks: list[DisplayTask]):
        self.tasks = tasks
        super().__init__()

    def make(self) -> LatexObject:
        tasks_list = Itemize()
        for task in self.tasks:
            tasks_list.add_item(OutlineTask(task))
        return tasks_list


class OutlineTasks(StatuslessTasks):
    _title = 'Tasks'


class NewTasks(StatuslessTasks):
    pass
