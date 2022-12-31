import typing

from sphinx.application import Sphinx

from .directive import SvgbobDirective
from .transform import SvgbobToImageTransform
from .node import Div


__version__ = "0.2.1"


def setup(app: Sphinx) -> typing.Dict[str, typing.Any]:
    app.add_node(Div,
        html=(Div.visit_div_html, Div.depart_div_html)
    )
    app.add_directive("svgbob", SvgbobDirective)
    app.add_transform(SvgbobToImageTransform)
    return {
        "version": __version__,
        "parallel_read_safe": True
    }
