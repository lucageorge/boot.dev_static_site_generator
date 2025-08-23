import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_that_two_text_nodes_are_equal_when_no_url_is_given(self):
        node1 = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node1, node2)
    
    def test_that_two_text_nodes_are_equal_when_same_arguments_are_given(self):
        node1 = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
        node2 = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
        self.assertEqual(node1, node2)
    
    def test_that_two_text_nodes_are_not_equal_when_text_is_different(self):
        node1 = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is another text node", TextType.BOLD)
        self.assertNotEqual(node1, node2)

    def test_that_two_text_nodes_are_not_equal_when_text_type_is_different(self):
        node1 = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is another text node", TextType.BOLD)
        self.assertNotEqual(node1, node2)

    def test_that_text_node_to_html_node_raises_value_error_when_text_type_is_invalid(self):
        node = TextNode("This is a text node", "invalid_text_type")
        with self.assertRaises(ValueError):
            TextNode.text_node_to_html_node(node)
    
    def test_text_node_to_html_node_is_ok_when_text_type_is_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = TextNode.text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.to_html(), "This is a text node")
    
    def test_text_node_to_html_node_is_ok_when_text_type_is_bold(self):
        node = TextNode("This is a text node", TextType.BOLD)
        html_node = TextNode.text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.to_html(), "<b>This is a text node</b>")
    
    def test_text_node_to_html_node_is_ok_when_text_type_is_italic(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        html_node = TextNode.text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.to_html(), "<i>This is a text node</i>")
    
    def test_text_node_to_html_node_is_ok_when_text_type_is_code(self):
        node = TextNode("This is a text node", TextType.CODE)
        html_node = TextNode.text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.to_html(), "<code>This is a text node</code>")
    
    def test_text_node_to_html_node_is_ok_when_text_type_is_link(self):
        node = TextNode("This is a text node", TextType.LINK, "https://www.boot.dev")
        html_node = TextNode.text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.to_html(), '<a href="https://www.boot.dev">This is a text node</a>')
    
    def test_text_node_to_html_node_is_ok_when_text_type_is_image(self):
        node = TextNode("This is a text node", TextType.IMAGE, "https://www.boot.dev")
        html_node = TextNode.text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.to_html(), '<img src="https://www.boot.dev" alt="This is a text node">')

if __name__ == "__main__":
    unittest.main()
