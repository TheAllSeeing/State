from pylatex import Section, Itemize
from pylatex.base_classes import LatexObject
from pylatex.section import Part

from statements.io.latex.latex_objects.long_goal import LongGoal
from statements.io.latex.latex_objects.markdown import Markdown
from statements.io.latex.latex_objects.plan import Schedule
from statements.io.latex.models.outline import LatexOutline
from statements.io.latex.utils.group import Group


class Outline(Group):
    def __init__(self, outline_model: LatexOutline):
        super().__init__()
        with self.create(Part(self.__class__.__name__)) as part:
            part.append(Markdown(outline_model.overview))

            with part.create(Section('Schedule')) as schedule_section:
                if outline_model.schedule:
                    schedule_section.append(Schedule(outline_model.schedule))
                else:
                    schedule_section.append('N/A')

            with part.create(Section('Goals')) as goals_section:
                if outline_model.goals:
                    with goals_section.create(Itemize()) as itemize:
                        for goal in outline_model.goals:
                            itemize.add_item(LongGoal(goal))
                else:
                    goals_section.append('N/A')
