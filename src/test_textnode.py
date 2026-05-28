import unittest
from textnode import TextNode, TextType, text_node_to_html_node

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node in bold", TextType.BOLD)
        node2 = TextNode("This is a text node in bold", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a text node in italic", TextType.ITALIC)
        node2 = TextNode("This is a text node in bold", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_url_eq(self):
        node = TextNode("This is a text node with a link", TextType.LINK, "https://www.boot.dev/")
        node2 = TextNode("This is a text node with a link", TextType.LINK, "https://www.boot.dev/")
        self.assertEqual(node, node2)

    def test_url_not_eq(self):
        node = TextNode("This is a text node with a link", TextType.LINK, "https://www.boot.dev/")
        node2 = TextNode("This is a text node with a link", TextType.LINK, "https://www.google.com/")
        self.assertNotEqual(node, node2)

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        node = TextNode("This is a text node in bold", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a text node in bold")

    def test_link_with_props(self):
        node = TextNode("This is a link node", TextType.LINK, url="https://www.boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This is a link node")
        props = {
            "href": "https://www.boot.dev"
        }
        self.assertEqual(html_node.props, props)

    def test_image_with_props(self):
        node = TextNode("This is a placeholder image", TextType.IMAGE, url="imageurl.com/image.png")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        props = {
            "src": "imageurl.com/image.png",
            "alt": "This is a placeholder image"
        }
        self.assertEqual(html_node.props, props)

if __name__ == "__main__":
    unittest.main()