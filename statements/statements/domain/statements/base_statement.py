import itertools
from functools import cached_property

from pydantic import BaseModel

from statements.domain.settings.aspect import Aspect
from statements.domain.settings.statement_config import StatementConfig


class Statement(BaseModel):
    config: StatementConfig
    aspects: list[Aspect]

    @cached_property
    def projects_to_aspects(self) -> dict[str, Aspect]:
        return {project: aspect for aspect
                in self.aspects for project
                in itertools.chain(aspect.active_projects, aspect.passive_projects,
                                   aspect.frozen_projects, aspect.archived_projects)}
