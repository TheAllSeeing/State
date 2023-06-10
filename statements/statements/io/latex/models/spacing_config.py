from pydantic import BaseModel


class LatexSpacingConfig(BaseModel):
    paragraph_skip: float
    paragraph_indent: float
    array_stretch: float
