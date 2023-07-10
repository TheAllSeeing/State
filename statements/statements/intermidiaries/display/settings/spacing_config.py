from pydantic import BaseModel


class DisplaySpacingConfig(BaseModel):
    paragraph_skip: float
    paragraph_indent: float
    array_stretch: float
