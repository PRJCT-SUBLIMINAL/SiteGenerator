from htmlnode import ParentNode, LeafNode
import unittest

class TestHTMLNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span>child</span></div>"
        )

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])

        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_greatgrandchildren(self):
        great_grandchild_node = LeafNode("b", "greatgrandchild")
        grandchild_node = ParentNode("span", [great_grandchild_node])
        child_node = ParentNode("a", [grandchild_node])
        parent_node = ParentNode("div", [child_node])

        self.assertEqual(
            parent_node.to_html(),
            "<div><a><span><b>greatgrandchild</b></span></a></div>"
        )

    def test_to_html_with_greatgrandchildren_and_props(self):
        props = {
            "href": "https://www.boot.dev/",
            "target": "__blank"
        }
        great_grandchild_node = LeafNode("a", "greatgrandchild", props)
        grandchild_node = ParentNode("span", [great_grandchild_node])
        child_node = ParentNode("b", [grandchild_node])
        parent_node = ParentNode("div", [child_node])

        self.assertEqual(
            parent_node.to_html(),
            '<div><b><span><a href="https://www.boot.dev/" target="__blank">greatgrandchild</a></span></b></div>'
        )
    

if __name__ == "__main__":
    unittest.main()