from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None, self_closing=False):
        super().__init__(tag, value, None, props)
        self.self_closing = self_closing
    
    def to_html(self):
        if not self.value and not self.self_closing:
            raise ValueError("Leaf node must have a value")
        if not self.tag:
            return self.value
        props = self.props_to_html()
        html = f"<{self.tag}{" " + props if props else ""}>"
        if not self.self_closing:
            html += f"{self.value}</{self.tag}>"
        return html


if __name__ == "__main__":
    print(LeafNode("p", "This is a paragraph of text.").to_html())
    print(LeafNode("a", "Click me!", {"href": "https://www.google.com"}).to_html())