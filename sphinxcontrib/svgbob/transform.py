import typing

import sphinx.transforms
from docutils.nodes import literal_block, raw

from ._svgbob import to_svg
from .node import svgbob, Div


class SvgbobToImageTransform(sphinx.transforms.SphinxTransform):
    """Sphinx transform to turn Svgbob nodes into SVG images.
    """

    default_priority = 10

    def builder_supports_svg(self) -> bool:
        return 'image/svg+xml' in self.app.builder.supported_image_types

    def apply(self, **kwargs: typing.Any) -> None:
        for node in self.document.traverse(svgbob):

            if self.builder_supports_svg():
                options = {
                    "font_size": node["options"].get("font-size"),
                    "font_family": node["options"].get("font-family"),
                    "fill_color": node["options"].get("fill-color"),
                    "background_color": node["options"].get("background-color"),
                    "stroke_color": node["options"].get("stroke-color"),
                    "stroke_width": node["options"].get("stroke-width"),
                    "scale": node["options"].get("scale"),
                }
                svg = self.render(node, options)
                svg_node = raw('', svg, format='html')

                container_svg_node = Div()
                container_svg_node += svg_node

                if "align" in node:
                    container_svg_node["style"] = f"text-align: {node['align']}"
                if "classes" in node:
                    container_svg_node["classes"] = node["classes"]
                node.replace_self(container_svg_node)

            else:
                rawnode = literal_block(node["code"], node["code"])
                node.replace_self(rawnode)

    def render(
        self,
        node: svgbob,
        options: typing.Dict[str, object],
    ) -> str:
        return to_svg(node["code"], **options)
