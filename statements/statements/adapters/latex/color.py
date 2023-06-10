from pydantic.color import Color

from statements.io.latex.models.color import LatexColor


class ColorAdapter:
    def get_latex_color(self, name: str, color: Color):
        red, green, blue = color.as_rgb_tuple()
        return LatexColor(
            name=name,
            red=red,
            green=green,
            blue=blue
        )
