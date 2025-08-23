from htmlnode import HTMLNode
from lefanode import LeafNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        if not self.tag:
            raise ValueError("Parent node must have a tag")
        if not self.children:
            raise ValueError("Parent node must have children")
        props = self.props_to_html()
        children = "".join([child.to_html() for child in self.children])
        return f"<{self.tag}{" " + props if props else ""}>{children}</{self.tag}>"

if __name__ == "__main__":
    node = ParentNode(
        "p",
        [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ],
    )
    html = node.to_html()
    print(html)
    assert(html == "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")