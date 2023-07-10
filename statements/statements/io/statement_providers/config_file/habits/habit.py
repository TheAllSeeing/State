from pydantic import BaseModel, Field, Extra


class HabitFrequency(BaseModel):
    count: int | None = None
    hop: int | None = None


class HabitDescription(BaseModel):
    id_: str = Field(alias='id')
    description: str
    frequency: HabitFrequency = HabitFrequency()

    class Config:
        extra = Extra.forbid


ScopeHabits = dict[str, list[HabitDescription]]


class HabitConfig(BaseModel):
    monthly: ScopeHabits = Field({}, alias='Monthly')
    weekly: ScopeHabits = Field({}, alias='Weekly')
    daily: ScopeHabits = Field({}, alias='Daily')
