from htmlnode import LeafNode
import unittest

class TestHTMLNode(unittest.TestCase):
    def test_p_element(self):
        node = LeafNode('p', 'Hello, world!')
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_link_element(self):
        props = {
            "href": "https://www.boot.dev",
            "target": "__blank"
        }
        node = LeafNode('a', 'Click here!', props)
        self.assertEqual(node.to_html(), '<a href="https://www.boot.dev" target="__blank">Click here!</a>')

    def test_no_tag(self):
        node = LeafNode(tag=None, value='Punjabi funk master punch')
        self.assertEqual(node.to_html(), "Punjabi funk master punch")

    

if __name__ == "__main__":
    unittest.main()