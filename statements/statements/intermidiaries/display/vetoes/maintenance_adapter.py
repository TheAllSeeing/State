from statements.domain.settings.aspect import Aspect
from statements.domain.vetoes.veto_maintenance import VetoMaintenance
from statements.intermidiaries.display.projects.adapter import ProjectAdapter
from statements.intermidiaries.display.vetoes.veto_maintenance import DisplayVetoMaintenance, DisplayVetoViolation


class VetoMaintenanceAdapter:
    def __init__(self, project_adapter: ProjectAdapter):
        self.project_adapter = project_adapter

    def get_display_veto_maintenance(self, veto_maintenance: VetoMaintenance, projects_to_aspects: dict[str, Aspect]) \
            -> DisplayVetoMaintenance:
        return DisplayVetoMaintenance(
            project=self.project_adapter.get_display_project(veto_maintenance.veto.project, projects_to_aspects),
            title=veto_maintenance.veto.description,
            violations=[
                DisplayVetoViolation(
                    time_point=violation.date_.strftime('%Y-%m-%d %A'),
                    detail=violation.detail
                )
                for violation in veto_maintenance.violations
            ]
        )
