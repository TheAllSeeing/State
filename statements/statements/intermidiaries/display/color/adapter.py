from pydantic.color import Color

from statements.intermidiaries.display.color.color import DisplayColor


class ColorAdapter:
    def get_display_color(self, name: str, color: Color):
        red, green, blue = color.as_rgb_tuple()
        return DisplayColor(
            name=name,
            red=red,
            green=green,
            blue=blue
        )
