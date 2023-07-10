from pydantic import BaseModel, Field


class StatusChangeDescription(BaseModel):
    project_stub: str = Field(alias='stub')
    change_description: str = Field(alias='description')


ChangeDescriptions = dict[str, StatusChangeDescription]


class ProjectStatusChangesConfig(BaseModel):
    new: ChangeDescriptions = Field(alias='New')
    thawed: ChangeDescriptions = Field(alias='Thawed')
    frozen: ChangeDescriptions = Field(alias='Frozen')
    closed: ChangeDescriptions = Field(alias='Closed')
