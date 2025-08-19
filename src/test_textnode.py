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


if __name__ == "__main__":
    unittest.main()
