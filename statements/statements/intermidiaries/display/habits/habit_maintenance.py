from typing import OrderedDict

from pydantic import BaseModel

from statements.intermidiaries.display.progress_status.progress_status import DisplayProgressStatus
from statements.intermidiaries.display.projects.project import DisplayProject


class DisplaySeriesMaintenance(BaseModel):
    title: str
    project: DisplayProject
    series: OrderedDict[str, DisplayProgressStatus]


class DisplayScopeMaintenance(BaseModel):
    title: str
    project: DisplayProject
    outer_scopes: list[str]
    inner_scopes: list[str]
    maintenance: OrderedDict[str, OrderedDict[str, DisplayProgressStatus]]
    


