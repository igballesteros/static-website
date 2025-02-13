import unittest

from texttohtml import text_node_to_html_node
from textnode import TextType, TextNode

class TestTextNode_to_HTMLNode(unittest.TestCase):

    def test_simple_node(self):
        text_node = TextNode("Hello, world!", TextType.TEXT)
        html_node = text_node_to_html_node(text_node)
        self.assertIsNone(html_node.tag)
        self.assertEqual(html_node.value, "Hello, world!")
        self.assertIsNone(html_node.props)

    def test_bold_node(self):
        text_node = TextNode("Hello, world!", TextType.BOLD)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "Hello, world!")
        self.assertIsNone(html_node.props)

    def test_link_node(self):
        text_node = TextNode("Click Me!", TextType.LINK, "https://igballesteros.com")
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "Click Me!")
        self.assertEqual(html_node.props, {"href":"https://igballesteros.com"})

    def test_image_node(self):
        text_node = TextNode("face image", TextType.IMAGE, "https://image.com")
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props, {"src":"https://image.com", "alt":"face image"})

    def test_invalid_node(self):
        text_node = TextNode("aaaaaa", None)
        # Use assertRaises to check that an exception is raised
        with self.assertRaises(Exception):
            text_node_to_html_node(text_node)


if __name__ == "__main__":
    unittest.main()