import os.path
from pathlib import Path

from statements.consts import TINYTEX_BIN_RELATIVE, APP_NAME
from statements.domain.settings.scope import StatementType
from statements.intermidiaries.display.color.adapter import ColorAdapter
from statements.intermidiaries.display.color.color import DisplayColor
from statements.intermidiaries.display.context.adapter import ContextAdapter
from statements.intermidiaries.display.day.adapter import DiaryAdapter, SleepAdapter, RestAdapter
from statements.intermidiaries.display.events.adapter import EventAdapter
from statements.intermidiaries.display.goals.adapter import GoalAdapter
from statements.intermidiaries.display.goals.closure_adapter import GoalClosureAdapter
from statements.intermidiaries.display.habits.adapter import HabitAdapter
from statements.intermidiaries.display.habits.maintenance_adapter import HabitMaintenanceAdapter
from statements.intermidiaries.display.incidents.adapter import IncidentAdapter
from statements.intermidiaries.display.issue.adapter import IssueAdapter
from statements.intermidiaries.display.long_goals.adapter import LongGoalAdapter
from statements.intermidiaries.display.long_goals.closure_adapter import LongGoalClosureAdapter
from statements.intermidiaries.display.parts.day.conclusions_adapter import DayConclusionsAdapter
from statements.intermidiaries.display.parts.day.outline_adapter import DayOutlineAdapter
from statements.intermidiaries.display.parts.day.results_adapter import DayResultsAdapter
from statements.intermidiaries.display.parts.day.status_adapter import DayStatusAdapter
from statements.intermidiaries.display.parts.month.conclusions_adapter import MonthConclusionsAdapter
from statements.intermidiaries.display.parts.month.outline_adapter import MonthOutlineAdapter
from statements.intermidiaries.display.parts.month.results_adapter import MonthResultsAdapter
from statements.intermidiaries.display.parts.month.status_adapter import MonthStatusAdapter
from statements.intermidiaries.display.parts.season.conclusions_adapter import SeasonConclusionsAdapter
from statements.intermidiaries.display.parts.season.outline_adapter import SeasonOutlineAdapter
from statements.intermidiaries.display.parts.season.results_adapter import SeasonResultsAdapter
from statements.intermidiaries.display.parts.season.status_adapter import SeasonStatusAdapter
from statements.intermidiaries.display.parts.week.conclusions_adapter import WeekConclusionsAdapter
from statements.intermidiaries.display.parts.week.outline_adapter import WeekOutlineAdapter
from statements.intermidiaries.display.parts.week.results_adapter import WeekResultsAdapter
from statements.intermidiaries.display.parts.week.status_adapter import WeekStatusAdapter
from statements.intermidiaries.display.progress_status.adapter import ProgressStatusAdapter
from statements.intermidiaries.display.projects.adapter import ProjectAdapter
from statements.intermidiaries.display.projects.status_change_adapter import ProjectStatusChangeAdapter
from statements.intermidiaries.display.proposals.adapter import ProposalAdapter
from statements.intermidiaries.display.settings.aspect_adapter import AspectAdapter
from statements.intermidiaries.display.settings.color_config import DisplayColorConfig
from statements.intermidiaries.display.settings.font_config import DisplayFontConfig
from statements.intermidiaries.display.settings.spacing_config import DisplaySpacingConfig
from statements.intermidiaries.display.settings.style import DisplayStatementStyle
from statements.intermidiaries.display.settings.title_config_adapter import TitleConfigAdapter
from statements.intermidiaries.display.statements.day.adapter import DailyStatementAdapter
from statements.intermidiaries.display.statements.month.adapter import MonthStatementAdapter
from statements.intermidiaries.display.statements.season.adapter import SeasonStatementAdapter
from statements.intermidiaries.display.statements.week.adapter import WeeklyStatementAdapter
from statements.intermidiaries.display.tasks.adapter import TaskAdapter
from statements.intermidiaries.display.vetoes.adapter import VetoAdapter
from statements.intermidiaries.display.vetoes.maintenance_adapter import VetoMaintenanceAdapter
from statements.io.entrypoints.typer.app import StateCLI
from statements.io.entrypoints.typer.commands import MakerCommands
from statements.io.statement_compiler.latex import DailyLatexCompiler, MonthlyLatexCompiler, SeasonLatexCompiler
from statements.io.statement_compiler.latex import WeeklyLatexCompiler
from statements.io.statement_providers.config_file.context.context import TOMLContextProvider
from statements.io.statement_providers.config_file.day.provider import TOMLDayProvider
from statements.io.statement_providers.config_file.events.timeline_provider import TOMLTimelineProvider
from statements.io.statement_providers.config_file.goals.adapter import InputGoalAdapter
from statements.io.statement_providers.config_file.goals.goal_conclusions_provider import TOMLGoalConclusionsProvider
from statements.io.statement_providers.config_file.goals.goals_provider import TOMLGoalsProvider
from statements.io.statement_providers.config_file.habits.maintenance_adapter import InputHabitMaintenanceAdapter
from statements.io.statement_providers.config_file.habits.maintenance_provider import \
    TOMLHabitMaintenanceProvider
from statements.io.statement_providers.config_file.habits.provider import TOMLHabitProvider
from statements.io.statement_providers.config_file.incidents.provider import TOMLIncidentProvider
from statements.io.statement_providers.config_file.issues.provider import TOMLIssueProvider
from statements.io.statement_providers.config_file.long_goals.adapter import InputLongGoalAdapter
from statements.io.statement_providers.config_file.long_goals.goal_conclusions_provider import \
    TOMLLongGoalConclusionsProvider
from statements.io.statement_providers.config_file.long_goals.long_goals_provider import TOMLLongGoalProvider
from statements.io.statement_providers.config_file.long_goals.overview import FileMarkdownProvider
from statements.io.statement_providers.config_file.progress_status.adapter import InputProgressStatusAdapter
from statements.io.statement_providers.config_file.project_changes.provider import TOMLProjectStatusChangeProvider
from statements.io.statement_providers.config_file.proposals.new_proposals_provider import TOMLNewProposalProvider
from statements.io.statement_providers.config_file.proposals.provider import TOMLProposalProvider
from statements.io.statement_providers.config_file.settings.aspects_provider import TOMLAspectsProvider
from statements.io.statement_providers.config_file.settings.settings_provider import TOMLStatementSettingsProvider
from statements.io.statement_providers.config_file.statements.daily_statement_provider import \
    FilesDailyStatementProvider
from statements.io.statement_providers.config_file.statements.monthly_statement_provider import \
    FilesMonthlyStatementProvider
from statements.io.statement_providers.config_file.statements.season_statement_provider import \
    FilesSeasonStatementProvider
from statements.io.statement_providers.config_file.statements.weekly_statement_provider import \
    FilesWeeklyStatementProvider
from statements.io.statement_providers.config_file.tasks.adapter import InputTaskAdapter
from statements.io.statement_providers.config_file.tasks.tasks_provider import TOMLTasksProvider
from statements.io.statement_providers.config_file.vetoes.maintenance_provider import TOMLVetoMaintenanceProvider
from statements.io.statement_providers.config_file.vetoes.provider import TOMLVetoesProvider
from statements.use_cases.statement_maker import StatementMaker

SETTINGS_DIR = Path('meta')
ORIENTATION_DIR = Path('orientation')
DOCUMENTATION_DIR = Path('documentation')
CONCLUSIONS_DIR = Path('conclusions')

input_progress_status_adapter = InputProgressStatusAdapter()
input_goal_adapter = InputGoalAdapter(status_adapter=input_progress_status_adapter)
input_long_goal_adapter = InputLongGoalAdapter(status_adapter=input_progress_status_adapter)
input_task_adapter = InputTaskAdapter(status_adapter=input_progress_status_adapter)

progress_status_adapter = ProgressStatusAdapter()
color_adapter = ColorAdapter()
project_adapter = ProjectAdapter(color_adapter=color_adapter)
proposal_adapter = ProposalAdapter(project_adapter=project_adapter)
goal_adapter = GoalAdapter(project_adapter=project_adapter,
                           progress_status_adapter=progress_status_adapter)
long_goal_adapter = LongGoalAdapter(project_adapter=project_adapter,
                                    progress_status_adapter=progress_status_adapter)
task_adapter = TaskAdapter(project_adapter=project_adapter,
                           progress_status_adapter=progress_status_adapter)
issue_adapter = IssueAdapter(project_adapter=project_adapter)


TINYTEX_BIN = Path(os.path.expanduser(f'~/.local/share/{APP_NAME}')) / TINYTEX_BIN_RELATIVE

app = StateCLI(
    name='state',
    season_commands=MakerCommands(
        type_=StatementType.SEASON,
        statement_maker=StatementMaker(
            provider=FilesSeasonStatementProvider(
                settings_provider=TOMLStatementSettingsProvider(file_path=SETTINGS_DIR / 'statement.toml'),
                aspects_provider=TOMLAspectsProvider(file_path=SETTINGS_DIR / 'projects.toml'),
                overview_provider=FileMarkdownProvider(file_path=ORIENTATION_DIR / 'overview.md'),
                schedule_provider=TOMLTimelineProvider(file_path=ORIENTATION_DIR / 'schedule.toml'),
                goals_provider=TOMLLongGoalProvider(file_path=ORIENTATION_DIR / 'long_goals.toml',
                                                    goal_adapter=input_long_goal_adapter),
                habits_provider=TOMLHabitProvider(file_path=ORIENTATION_DIR / 'habits.toml'),
                vetoes_provider=TOMLVetoesProvider(file_path=ORIENTATION_DIR / 'vetoes.toml'),
                plan_provider=TOMLTimelineProvider(file_path=ORIENTATION_DIR / 'timeline.toml'),
                issues_provider=TOMLIssueProvider(file_path=DOCUMENTATION_DIR / 'issues.toml'),
                proposals_provider=TOMLProposalProvider(file_path=ORIENTATION_DIR / 'proposals.toml'),
                incidents_provider=TOMLIncidentProvider(file_path=DOCUMENTATION_DIR / 'incidents.toml'),
                context_provider=TOMLContextProvider(file_path=DOCUMENTATION_DIR / 'context.toml'),
                veto_maintenance_provider=TOMLVetoMaintenanceProvider(
                    file_path=DOCUMENTATION_DIR / 'veto_maintenance.toml'),
                new_issues_provider=TOMLIssueProvider(file_path=DOCUMENTATION_DIR / 'new_issues.toml'),
                project_status_changes_provider=TOMLProjectStatusChangeProvider(
                    file_path=CONCLUSIONS_DIR / 'projects.toml'),
                goal_conclusions_provider=TOMLLongGoalConclusionsProvider(file_path=CONCLUSIONS_DIR / 'goals.toml',
                                                                          goals_adapter=input_long_goal_adapter),
                new_proposals_provider=TOMLNewProposalProvider(file_path=CONCLUSIONS_DIR / 'proposals.toml'),
                notes_provider=FileMarkdownProvider(file_path=CONCLUSIONS_DIR / 'notes.md')
            ),
            compiler=SeasonLatexCompiler(
                SeasonStatementAdapter(
                    outline_adapter=SeasonOutlineAdapter(
                        goal_adapter=long_goal_adapter,
                        event_adapter=EventAdapter(project_adapter=project_adapter),
                        habit_adapter=HabitAdapter(project_adapter=project_adapter),
                        veto_adapter=VetoAdapter(project_adapter=project_adapter)
                    ),
                    status_adapter=SeasonStatusAdapter(
                        goal_adapter=long_goal_adapter,
                        issue_adapter=issue_adapter,
                        proposal_adapter=proposal_adapter
                    ),
                    results_adapter=SeasonResultsAdapter(
                        incident_adapter=IncidentAdapter(project_adapter=project_adapter),
                        context_adapter=ContextAdapter(project_adapter=project_adapter),
                        habit_maintenance_adapter=HabitMaintenanceAdapter(project_adapter=project_adapter,
                                                                          progress_status_adapter=ProgressStatusAdapter()),
                        veto_maintenance_adapter=VetoMaintenanceAdapter(project_adapter=project_adapter),
                        goals_adapter=long_goal_adapter,
                        proposal_adapter=proposal_adapter,
                        issue_adapter=issue_adapter
                    ),
                    conclusions_adapter=SeasonConclusionsAdapter(
                        project_status_change_adapter=ProjectStatusChangeAdapter(project_adapter=project_adapter),
                        goal_adapter=long_goal_adapter,
                        goal_closure_adapter=LongGoalClosureAdapter(goal_adapter=long_goal_adapter),
                        proposal_adapter=proposal_adapter
                    ),
                    aspects_adapter=AspectAdapter(color_adapter=color_adapter),
                    title_adapter=TitleConfigAdapter(),
                    statement_style=DisplayStatementStyle(
                        spacing_config=DisplaySpacingConfig(
                            paragraph_indent=0,
                            paragraph_skip=1,
                            array_stretch=1.5
                        ),
                        color_config=DisplayColorConfig(
                            text_color=DisplayColor(name='TextColor', red=217, green=217, blue=217),
                            page_color=DisplayColor(name='PageColor', red=82, green=82, blue=82),
                            link_color=DisplayColor(name='LinkColor', red=154, green=205, blue=50)
                        ),
                        font_config=DisplayFontConfig(
                            font_family='charter'
                        )
                    )
                ),
                tinytex_bin=TINYTEX_BIN
            )
        )
    ),
    month_commands=MakerCommands(
        type_=StatementType.MONTH,
        statement_maker=StatementMaker(
            provider=FilesMonthlyStatementProvider(
                settings_provider=TOMLStatementSettingsProvider(file_path=SETTINGS_DIR / 'statement.toml'),
                aspects_provider=TOMLAspectsProvider(file_path=SETTINGS_DIR / 'projects.toml'),
                schedule_provider=TOMLTimelineProvider(file_path=ORIENTATION_DIR / 'schedule.toml'),
                goals_provider=TOMLGoalsProvider(file_path=ORIENTATION_DIR / 'goals.toml',
                                                 goal_adapter=input_goal_adapter),
                habits_provider=TOMLHabitProvider(file_path=ORIENTATION_DIR / 'habits.toml'),
                vetoes_provider=TOMLVetoesProvider(file_path=ORIENTATION_DIR / 'vetoes.toml'),
                plan_provider=TOMLTimelineProvider(file_path=ORIENTATION_DIR / 'timeline.toml'),
                issues_provider=TOMLIssueProvider(file_path=DOCUMENTATION_DIR / 'issues.toml'),
                proposals_provider=TOMLProposalProvider(file_path=ORIENTATION_DIR / 'proposals.toml'),
                incidents_provider=TOMLIncidentProvider(file_path=DOCUMENTATION_DIR / 'incidents.toml'),
                context_provider=TOMLContextProvider(file_path=DOCUMENTATION_DIR / 'context.toml'),
                habit_maintenance_provider=TOMLHabitMaintenanceProvider(
                    file_path=DOCUMENTATION_DIR / 'habit_maintenance.toml',
                    maintenance_adapter=InputHabitMaintenanceAdapter(
                        status_adapter=input_progress_status_adapter
                    )),
                veto_maintenance_provider=TOMLVetoMaintenanceProvider(
                    file_path=DOCUMENTATION_DIR / 'veto_maintenance.toml'),
                new_issues_provider=TOMLIssueProvider(file_path=DOCUMENTATION_DIR / 'new_issues.toml'),
                goal_conclusions_provider=TOMLGoalConclusionsProvider(file_path=CONCLUSIONS_DIR / 'goals.toml',
                                                                      goals_adapter=input_goal_adapter),
                new_proposals_provider=TOMLNewProposalProvider(file_path=CONCLUSIONS_DIR / 'proposals.toml'),
                notes_provider=FileMarkdownProvider(file_path=CONCLUSIONS_DIR / 'notes.md')
            ),
            compiler=MonthlyLatexCompiler(
                MonthStatementAdapter(
                    outline_adapter=MonthOutlineAdapter(
                        goal_adapter=goal_adapter,
                        event_adapter=EventAdapter(project_adapter=project_adapter),
                        habit_adapter=HabitAdapter(project_adapter=project_adapter),
                        veto_adapter=VetoAdapter(project_adapter=project_adapter)
                    ),
                    status_adapter=MonthStatusAdapter(
                        goal_adapter=goal_adapter,
                        issue_adapter=issue_adapter,
                        proposal_adapter=proposal_adapter
                    ),
                    results_adapter=MonthResultsAdapter(
                        incident_adapter=IncidentAdapter(project_adapter=project_adapter),
                        context_adapter=ContextAdapter(project_adapter=project_adapter),
                        habit_maintenance_adapter=HabitMaintenanceAdapter(project_adapter=project_adapter,
                                                                          progress_status_adapter=ProgressStatusAdapter()),
                        veto_maintenance_adapter=VetoMaintenanceAdapter(project_adapter=project_adapter),
                        goals_adapter=goal_adapter,
                        proposal_adapter=proposal_adapter,
                        issue_adapter=issue_adapter
                    ),
                    conclusions_adapter=MonthConclusionsAdapter(
                        goal_adapter=goal_adapter,
                        goal_closure_adapter=GoalClosureAdapter(goal_adapter=goal_adapter),
                        proposal_adapter=proposal_adapter
                    ),
                    aspects_adapter=AspectAdapter(color_adapter=color_adapter),
                    title_adapter=TitleConfigAdapter(),
                    statement_style=DisplayStatementStyle(
                        spacing_config=DisplaySpacingConfig(
                            paragraph_indent=0,
                            paragraph_skip=1,
                            array_stretch=1.5
                        ),
                        color_config=DisplayColorConfig(
                            text_color=DisplayColor(name='TextColor', red=217, green=217, blue=217),
                            page_color=DisplayColor(name='PageColor', red=82, green=82, blue=82),
                            link_color=DisplayColor(name='LinkColor', red=154, green=205, blue=50)
                        ),
                        font_config=DisplayFontConfig(
                            font_family='charter'
                        )
                    )
                ),
                tinytex_bin=TINYTEX_BIN
            )
        )
    ),
    week_commands=MakerCommands(
        type_=StatementType.WEEK,
        statement_maker=StatementMaker(
            provider=FilesWeeklyStatementProvider(
                settings_provider=TOMLStatementSettingsProvider(file_path=SETTINGS_DIR / 'statement.toml'),
                aspects_provider=TOMLAspectsProvider(file_path=SETTINGS_DIR / 'projects.toml'),
                schedule_provider=TOMLTimelineProvider(file_path=ORIENTATION_DIR / 'schedule.toml'),
                goals_provider=TOMLGoalsProvider(file_path=ORIENTATION_DIR / 'goals.toml',
                                                 goal_adapter=input_goal_adapter),
                tasks_provider=TOMLTasksProvider(file_path=ORIENTATION_DIR / 'tasks.toml',
                                                 task_adapter=input_task_adapter),
                habits_provider=TOMLHabitProvider(file_path=ORIENTATION_DIR / 'habits.toml'),
                vetoes_provider=TOMLVetoesProvider(file_path=ORIENTATION_DIR / 'vetoes.toml'),
                plan_provider=TOMLTimelineProvider(file_path=ORIENTATION_DIR / 'timeline.toml'),
                issues_provider=TOMLIssueProvider(file_path=DOCUMENTATION_DIR / 'issues.toml'),
                proposals_provider=TOMLProposalProvider(file_path=ORIENTATION_DIR / 'proposals.toml'),
                incidents_provider=TOMLIncidentProvider(file_path=DOCUMENTATION_DIR / 'incidents.toml'),
                context_provider=TOMLContextProvider(file_path=DOCUMENTATION_DIR / 'context.toml'),
                habit_maintenance_provider=TOMLHabitMaintenanceProvider(
                    file_path=DOCUMENTATION_DIR / 'habit_maintenance.toml',
                    maintenance_adapter=InputHabitMaintenanceAdapter(
                        status_adapter=input_progress_status_adapter
                    )),
                veto_maintenance_provider=TOMLVetoMaintenanceProvider(
                    file_path=DOCUMENTATION_DIR / 'veto_maintenance.toml'),
                new_issues_provider=TOMLIssueProvider(file_path=DOCUMENTATION_DIR / 'new_issues.toml'),
                new_goals_provider=TOMLGoalsProvider(CONCLUSIONS_DIR / 'goals.toml', goal_adapter=input_goal_adapter),
                new_tasks_provider=TOMLTasksProvider(CONCLUSIONS_DIR / 'tasks.toml', task_adapter=input_task_adapter),
                new_proposals_provider=TOMLNewProposalProvider(file_path=CONCLUSIONS_DIR / 'proposals.toml'),
                notes_provider=FileMarkdownProvider(file_path=CONCLUSIONS_DIR / 'notes.md')
            ),
            compiler=WeeklyLatexCompiler(
                WeeklyStatementAdapter(
                    outline_adapter=WeekOutlineAdapter(
                        goal_adapter=goal_adapter,
                        task_adapter=task_adapter,
                        event_adapter=EventAdapter(project_adapter=project_adapter),
                        habit_adapter=HabitAdapter(project_adapter=project_adapter),
                        veto_adapter=VetoAdapter(project_adapter=project_adapter)
                    ),
                    status_adapter=WeekStatusAdapter(
                        goal_adapter=goal_adapter,
                        task_adapter=task_adapter,
                        issue_adapter=issue_adapter,
                        proposal_adapter=proposal_adapter
                    ),
                    results_adapter=WeekResultsAdapter(
                        incident_adapter=IncidentAdapter(project_adapter=project_adapter),
                        context_adapter=ContextAdapter(project_adapter=project_adapter),
                        habit_maintenance_adapter=HabitMaintenanceAdapter(project_adapter=project_adapter,
                                                                          progress_status_adapter=ProgressStatusAdapter()),
                        veto_maintenance_adapter=VetoMaintenanceAdapter(project_adapter=project_adapter),
                        task_adapter=task_adapter,
                        proposal_adapter=proposal_adapter,
                        issue_adapter=issue_adapter
                    ),
                    conclusions_adapter=WeekConclusionsAdapter(
                        goal_adapter=goal_adapter,
                        task_adapter=task_adapter,
                        proposal_adapter=proposal_adapter
                    ),
                    aspects_adapter=AspectAdapter(color_adapter=color_adapter),
                    title_adapter=TitleConfigAdapter(),
                    statement_style=DisplayStatementStyle(
                        spacing_config=DisplaySpacingConfig(
                            paragraph_indent=0,
                            paragraph_skip=1,
                            array_stretch=1.5
                        ),
                        color_config=DisplayColorConfig(
                            text_color=DisplayColor(name='TextColor', red=217, green=217, blue=217),
                            page_color=DisplayColor(name='PageColor', red=82, green=82, blue=82),
                            link_color=DisplayColor(name='LinkColor', red=154, green=205, blue=50)
                        ),
                        font_config=DisplayFontConfig(
                            font_family='charter'
                        )
                    )
                ),
                tinytex_bin=TINYTEX_BIN
            )
        )
    ),
    day_commands=MakerCommands(
        type_=StatementType.DAY,
        statement_maker=StatementMaker(
            provider=FilesDailyStatementProvider(
                settings_provider=TOMLStatementSettingsProvider(file_path=SETTINGS_DIR / 'statement.toml'),
                aspects_provider=TOMLAspectsProvider(file_path=SETTINGS_DIR / 'projects.toml'),
                schedule_provider=TOMLTimelineProvider(file_path=ORIENTATION_DIR / 'schedule.toml'),
                tasks_provider=TOMLTasksProvider(file_path=ORIENTATION_DIR / 'tasks.toml',
                                                 task_adapter=input_task_adapter),
                vetoes_provider=TOMLVetoesProvider(file_path=ORIENTATION_DIR / 'vetoes.toml'),
                plan_provider=TOMLTimelineProvider(file_path=ORIENTATION_DIR / 'timeline.toml'),
                day_provider=TOMLDayProvider(file_path=DOCUMENTATION_DIR / 'day.toml'),
                issues_provider=TOMLIssueProvider(file_path=DOCUMENTATION_DIR / 'issues.toml'),
                proposals_provider=TOMLProposalProvider(file_path=ORIENTATION_DIR / 'proposals.toml'),
                incidents_provider=TOMLIncidentProvider(file_path=DOCUMENTATION_DIR / 'incidents.toml'),
                context_provider=TOMLContextProvider(file_path=DOCUMENTATION_DIR / 'context.toml'),
                new_issues_provider=TOMLIssueProvider(file_path=DOCUMENTATION_DIR / 'new_issues.toml'),
                new_tasks_provider=TOMLTasksProvider(CONCLUSIONS_DIR / 'tasks.toml', task_adapter=input_task_adapter),
                new_proposals_provider=TOMLNewProposalProvider(file_path=CONCLUSIONS_DIR / 'proposals.toml'),
                notes_provider=FileMarkdownProvider(file_path=CONCLUSIONS_DIR / 'notes.md')
            ),
            compiler=DailyLatexCompiler(
                DailyStatementAdapter(
                    outline_adapter=DayOutlineAdapter(
                        task_adapter=task_adapter,
                        event_adapter=EventAdapter(project_adapter=project_adapter),
                        veto_adapter=VetoAdapter(project_adapter=project_adapter)
                    ),
                    status_adapter=DayStatusAdapter(
                        task_adapter=task_adapter,
                        issue_adapter=issue_adapter,
                        proposal_adapter=proposal_adapter
                    ),
                    results_adapter=DayResultsAdapter(
                        incident_adapter=IncidentAdapter(project_adapter=project_adapter),
                        context_adapter=ContextAdapter(project_adapter=project_adapter),
                        diary_adapter=DiaryAdapter(),
                        sleep_adapter=SleepAdapter(),
                        rest_adapter=RestAdapter(),
                        task_adapter=task_adapter,
                        proposal_adapter=proposal_adapter,
                        issue_adapter=issue_adapter
                    ),
                    conclusions_adapter=DayConclusionsAdapter(
                        task_adapter=task_adapter,
                        proposal_adapter=proposal_adapter
                    ),
                    aspects_adapter=AspectAdapter(color_adapter=color_adapter),
                    title_adapter=TitleConfigAdapter(),
                    statement_style=DisplayStatementStyle(
                        spacing_config=DisplaySpacingConfig(
                            paragraph_indent=0,
                            paragraph_skip=1,
                            array_stretch=1
                        ),
                        color_config=DisplayColorConfig(
                            text_color=DisplayColor(name='TextColor', red=217, green=217, blue=217),
                            page_color=DisplayColor(name='PageColor', red=82, green=82, blue=82),
                            link_color=DisplayColor(name='LinkColor', red=154, green=205, blue=50)
                        ),
                        font_config=DisplayFontConfig(
                            font_family='charter'
                        )
                    )
                ),
                tinytex_bin=TINYTEX_BIN
            )
        )
    )
)
