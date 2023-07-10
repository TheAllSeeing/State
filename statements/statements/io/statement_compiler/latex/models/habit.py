from statements.intermidiaries.display.habits.habit import DisplayHabit
from statements.io.statement_compiler.latex.utils.insight import Insight


class Habit(Insight):
    def __init__(self, habit_model: DisplayHabit):
        if habit_model.hop and habit_model.count:
            frequency = f'{habit_model.count}/{habit_model.hop} {habit_model.frequency[:-2]}s'
        elif habit_model.hop:
            frequency = f'every {habit_model.hop} {habit_model.frequency[:-2].lower()}s'
        elif habit_model.count:
            frequency = f'{habit_model.count}/{habit_model.frequency[:-2]}'
        else:
            frequency = habit_model.frequency

        super().__init__(habit_model.project,
                         f'{habit_model.description}, {frequency}',
                         id_=habit_model.id_)
