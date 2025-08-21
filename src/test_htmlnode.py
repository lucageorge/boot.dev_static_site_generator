import unittest

from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_that_to_html_raises_not_implemented_error(self):
        node = HTMLNode()
        with self.assertRaises(NotImplementedError):
            node.to_html()
    
    def test_that_props_to_html_returns_empty_string_when_no_props_are_given(self):
        node = HTMLNode()
        self.assertEqual(node.props_to_html(), "")
    
    def test_that_props_to_html_returns_string_when_props_are_given(self):
        props = {
            "href": "https://www.google.com",
            "target": "_blank",
        }
        node = HTMLNode(props=props)
        self.assertEqual(node.props_to_html(), 'href="https://www.google.com" target="_blank"') 

class TextLeafNode(unittest.TestCase):
    def test_leaf_to_html_when_no_props_are_given(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_lefa_to_html_when_props_are_given(self):
        props = {
            "href": "https://www.google.com",
            "target": "_blank",
        }
        node = LeafNode("a", "Click me!", props)
        self.assertEqual(node.to_html(), '<a href="https://www.google.com" target="_blank">Click me!</a>')

    def test_that_ValueError_is_raised_when_no_value_is_given(self):
        with self.assertRaises(ValueError):
            LeafNode("p", None).to_html()
    
    def test_that_text_is_returned_if_no_tag_is_given(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

if __name__ == "__main__":
    unittest.main()
