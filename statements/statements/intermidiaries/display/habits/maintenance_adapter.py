from statements.domain.settings.aspect import Aspect
from statements.domain.habits.habit_maintenance import HabitMaintenance, SeriesMaintenance, ScopeSeriesMaintenance
from statements.intermidiaries.display.progress_status.adapter import ProgressStatusAdapter
from statements.intermidiaries.display.projects.adapter import ProjectAdapter
from statements.intermidiaries.display.habits.habit_maintenance import DisplaySeriesMaintenance, DisplayScopeMaintenance


class HabitMaintenanceAdapter:
    def __init__(self, project_adapter: ProjectAdapter, progress_status_adapter: ProgressStatusAdapter):
        self.project_adapter = project_adapter
        self.progress_status_adapter = progress_status_adapter

    def get_display_maintenance(self, maintenance: HabitMaintenance, projects_to_aspects: dict[str, Aspect]) \
            -> DisplayScopeMaintenance | DisplaySeriesMaintenance:
        if isinstance(maintenance.maintenance, SeriesMaintenance):
            return DisplaySeriesMaintenance(
                title=maintenance.habit.description,
                project=self.project_adapter.get_display_project(maintenance.habit.project, projects_to_aspects),
                series={scope: self.progress_status_adapter.get_progress_status(status)
                        for scope, status in maintenance.maintenance.root.items()}
            )
        elif isinstance(maintenance.maintenance, ScopeSeriesMaintenance):
            return DisplayScopeMaintenance(
                title=maintenance.habit.description,
                project=self.project_adapter.get_display_project(maintenance.habit.project, projects_to_aspects),
                outer_scopes=maintenance.maintenance.root.keys(),
                inner_scopes=max(maintenance.maintenance.root.values(),
                                 key=lambda series: len(series.root.keys())).root.keys(),
                maintenance={scope: {series_key: self.progress_status_adapter.get_progress_status(status)
                                     for series_key, status in series.root.items()}
                             for scope, series in maintenance.maintenance.root.items()}
            )
        else:
            raise NotImplementedError(f'Unsupported maintenance type: {maintenance.maintenance.__class__.__name__}')
