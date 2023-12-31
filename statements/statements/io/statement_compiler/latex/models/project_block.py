from pylatex.base_classes import Command
from pylatex.basic import HFill, TextColor

from statements.intermidiaries.display.projects.project import DisplayProject
from statements.io.statement_compiler.latex.wrappers.break_ import Break
from statements.io.statement_compiler.latex.wrappers.group import Group

LINE_SIZE = 4
ACTIVE_MODIFIER = Command('bfseries')
PASSIVE_MODIFIER = Command('em')


class ProjectBlock(Group):
    def __init__(self, projects: list[DisplayProject], *, active: bool, line_size=LINE_SIZE):
        super().__init__()
        if active:
            self.append(ACTIVE_MODIFIER)
        else:
            self.append(PASSIVE_MODIFIER)

        chunks_count = len(projects) // line_size

        if len(projects) % line_size != 0:
            chunks_count += 1

        project_chunks = [projects[line_size * i:line_size * (i + 1)]
                          for i in range(chunks_count)]

        for i, chunk in enumerate(project_chunks, 1):

            for j, project in enumerate(chunk, 1):
                self.append(TextColor(project.color.name, project.name))
                if j != len(chunk):
                    self.append(HFill())

            if i != len(project_chunks):
                self.append(Break())