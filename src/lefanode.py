from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)
    
    def to_html(self):
        if not self.value:
            raise ValueError("Leaf node must have a value")
        if not self.tag:
            return self.value
        props = self.props_to_html()
        return f"<{self.tag}{" " + props if props else ""}>{self.value}</{self.tag}>"

if __name__ == "__main__":
    print(LeafNode("p", "This is a paragraph of text.").to_html())
    print(LeafNode("a", "Click me!", {"href": "https://www.google.com"}).to_html())