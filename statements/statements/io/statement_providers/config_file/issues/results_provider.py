from abc import ABC, abstractmethod

from pydantic import BaseModel

from statements.domain.issue import Issue
from statements.io.statement_providers.config_file.issues.issue_results import InputIssueResults
from statements.io.statement_providers.config_file.toml_provider import TOMLProvider


class IssueResults(BaseModel):
    closed: list[Issue]
    opened: list[Issue]


class IssueResultsProvider(ABC):
    @abstractmethod
    def get_issue_results(self) -> IssueResults:
        pass


class TOMLIssueResultsProvider(IssueResultsProvider, TOMLProvider):
    def get_issue_results(self) -> IssueResults:
        raw_data = self._get_raw_data()
        input_results = InputIssueResults.model_validate(raw_data)
        return IssueResults(
            closed=[
                Issue(
                    id_=issue.id_,
                    project=project,
                    title=issue.title,
                    description=issue.description,
                    note=issue.note
                )
                for project, project_issues in input_results.closed.items()
                for issue in project_issues
            ],
            opened=[
                Issue(
                    id_=issue.id_,
                    project=project,
                    title=issue.title,
                    description=issue.description,
                    note=issue.note
                )
                for project, project_issues in input_results.new.items()
                for issue in project_issues
            ],
        )
