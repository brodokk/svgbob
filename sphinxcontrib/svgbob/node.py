from docutils.nodes import Element, General, Inline, Node


class Div(General, Element):

    @staticmethod
    def visit_div_html(self, node: Element) -> None:
        attrs = {}
        for attr in node.attributes.keys():
            if node.attributes[attr]:
                attrs[attr] = node.attributes[attr]
        self.body.append(self.starttag(node, 'div', '', **attrs))

    @staticmethod
    def depart_div_html(self, node: Element = None) -> None:
        self.body.append('</div>\n')


class svgbob(General, Inline, Element):
    pass
