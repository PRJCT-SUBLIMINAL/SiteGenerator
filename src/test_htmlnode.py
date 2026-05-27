from htmlnode import HTMLNode
import unittest

class TestHTMLNode(unittest.TestCase):
    def test_eq_props_none(self):
        node = HTMLNode(props=None)
        self.assertEqual(node.props_to_html(), "")

    def test_eq_props_nothing(self):
        node = HTMLNode()
        self.assertEqual(node.props_to_html(), "")

    def test_eq_props(self) :
        node = HTMLNode(props={"href": "styles.css", "target": "__blank"})
        self.assertEqual(node.props_to_html(), ' href="styles.css" target="__blank"')

if __name__ == "__main__":
    unittest.main()