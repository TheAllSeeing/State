from pylatex.base_classes import LatexObject
from pylatex.base_classes.containers import Fragment

from statements.intermidiaries.display.incidents.incident import DisplayIncident
from statements.io.statement_compiler.latex.wrappers import MedSkip
from statements.io.statement_compiler.latex.models.incident import Incident
from statements.io.statement_compiler.latex.sections.base_section import BaseSection


class Incidents(BaseSection):
    def __init__(self, incidents: list[DisplayIncident]):
        self.incidents = incidents
        super().__init__()

    def make(self) -> LatexObject:
        fragment = Fragment()
        for incident in self.incidents:
            fragment.append(Incident(incident))
            fragment.append(MedSkip())
        return fragment
