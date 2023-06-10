import itertools
from functools import cached_property

from pydantic import BaseModel, computed_field

from statements.domain.outline.outline import Outline
from statements.domain.settings.aspect import Aspect
from statements.domain.settings.statement import StatementConfig


class Statement(BaseModel):
    config: StatementConfig
    aspects: list[Aspect]
    outline: Outline

    @cached_property
    def projects_to_aspects(self):
        return {project: aspect for aspect
                in self.aspects for project
                in itertools.chain(aspect.active_projects, aspect.passive_projects,
                                   aspect.frozen_projects, aspect.archived_projects)}

