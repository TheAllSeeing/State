from pylatex import Itemize
from pylatex.base_classes import LatexObject

from statements.intermidiaries.display.habits.habit import DisplayHabit
from statements.io.statement_compiler.latex.models.habit import Habit
from statements.io.statement_compiler.latex.sections.base_section import BaseSection


class Habits(BaseSection):
    def __init__(self, habits: list[DisplayHabit]):
        self.habits = habits
        super().__init__()

    def make(self) -> LatexObject:
        habit_list = Itemize()
        for habit in self.habits:
            habit_list.add_item(Habit(habit))
        return habit_list
