from pydantic import BaseModel

from statements.intermidiaries.display.color.color import DisplayColor


class DisplayColorConfig(BaseModel):
    text_color: DisplayColor
    page_color: DisplayColor
    link_color: DisplayColor
