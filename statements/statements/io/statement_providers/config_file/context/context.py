from abc import ABC, abstractmethod

from statements.domain.incidents.context import ContextItem
from statements.io.statement_providers.config_file.toml_provider import TOMLProvider


class ContextProvider(ABC):
    @abstractmethod
    def get_context_items(self) -> list[ContextItem]:
        pass


class TOMLContextProvider(ContextProvider, TOMLProvider):
    def get_context_items(self) -> list[ContextItem]:
        raw_context_items = self._get_raw_data()
        return [ContextItem(project=project, description=context)
                for project, project_contexts in raw_context_items.items()
                for context in project_contexts]
