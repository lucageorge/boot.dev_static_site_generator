import unittest

from htmlnode import HTMLNode

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



if __name__ == "__main__":
    unittest.main()
