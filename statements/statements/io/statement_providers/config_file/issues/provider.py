from abc import ABC, abstractmethod

from pydantic import TypeAdapter, BaseModel

from statements.domain.issue import Issue
from statements.io.statement_providers.config_file.issues.issue import InputIssue
from statements.io.statement_providers.config_file.toml_provider import TOMLProvider


class InputIssues(BaseModel):
    open: list[Issue]
    resolved: list[Issue]


class IssuesProvider(ABC):
    @abstractmethod
    def get_issues(self) -> InputIssues:
        pass


class TOMLIssueProvider(IssuesProvider, TOMLProvider):
    def get_issues(self) -> InputIssues:
        raw_issues = self._get_raw_data()
        config_issues = TypeAdapter(dict[str, list[InputIssue]]).validate_python(raw_issues)
        return InputIssues(
            open=[
                Issue(
                    id_=issue.id_,
                    project=project,
                    title=issue.title,
                    description=issue.description,
                    note=issue.note
                )
                for project, project_issues in config_issues.items()
                for issue in project_issues
                if not issue.resolved
            ],
            resolved=[
                Issue(
                    id_=issue.id_,
                    project=project,
                    title=issue.title,
                    description=issue.description,
                    note=issue.note
                )
                for project, project_issues in config_issues.items()
                for issue in project_issues
                if issue.resolved
            ]
        )
