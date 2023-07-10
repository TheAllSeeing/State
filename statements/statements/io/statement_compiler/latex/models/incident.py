import re

from pylatex.utils import bold

from statements.intermidiaries.display.incidents.incident import DisplayIncident
from statements.io.statement_compiler.latex.wrappers import Color
from statements.io.statement_compiler.latex.wrappers.group import Group
from statements.io.statement_compiler.latex.wrappers.new_paragraph import NewParagraph
from statements.io.statement_compiler.latex.utils.insight import Insight
from statements.io.statement_compiler.latex.utils.markdown import Markdown

START_TAB = re.compile(r'^ {4}', re.MULTILINE)


class Incident(Group):
    def __init__(self, incident: DisplayIncident):
        super().__init__()
        self.append(Color(incident.project.color.name))
        self.append(Insight(incident.project, bold(incident.title), id_=incident.id_))
        self.append(NewParagraph())
        self.append(Markdown(START_TAB.sub('', incident.description)))
