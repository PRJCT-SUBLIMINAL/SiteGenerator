import unittest
from textnode import TextNode, TextType

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

if __name__ == "__main__":
    unittest.main()