import unittest

from lefanode import LeafNode

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

    def test_leaf_to_html_when_self_closing_is_given(self):
        node = LeafNode("img", None, props={"src": "https://www.example.com", "alt": "Example.com"}, self_closing=True)
        self.assertEqual(node.to_html(), '<img src="https://www.example.com" alt="Example.com">')

    def test_that_ValueError_is_raised_when_no_value_is_given(self):
        with self.assertRaises(ValueError):
            LeafNode("p", None).to_html()
    
    def test_that_text_is_returned_if_no_tag_is_given(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

if __name__ == "__main__":
    unittest.main()