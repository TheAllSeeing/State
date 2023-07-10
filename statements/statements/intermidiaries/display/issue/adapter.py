from statements.domain.settings.aspect import Aspect
from statements.domain.issue import Issue
from statements.intermidiaries.display.issue.issue import DisplayIssue
from statements.intermidiaries.display.projects.adapter import ProjectAdapter


class IssueAdapter:
    def __init__(self, project_adapter: ProjectAdapter):
        self.project_adapter = project_adapter

    def get_display_issue(self, issue: Issue, projects_to_aspects: dict[str, Aspect]) -> DisplayIssue:
        return DisplayIssue(
            id_=issue.id_,
            project=self.project_adapter.get_display_project(issue.project, projects_to_aspects),
            title=issue.title,
            description=issue.description,
            note=issue.note
        )
