import unittest
from textnode import TextNode, TextType
from splitnodes_delimiter import split_nodes_delimiter

class TestTextNode(unittest.TestCase):
    def test_italic_delimiter(self):
        nodes = [
            TextNode("This is a _crazy_ world", TextType.TEXT),
            TextNode("Are you _insane_?", TextType.TEXT),
            # TextNode("Woah! Watch out he's an _evil_ man!", TextType.ITALIC)
        ]

        new_nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)

        self.assertEqual(new_nodes, [
            TextNode("This is a ", TextType.TEXT),
            TextNode("crazy", TextType.ITALIC),
            TextNode(" world", TextType.TEXT),
            TextNode("Are you ", TextType.TEXT),
            TextNode("insane", TextType.ITALIC),
            TextNode("?", TextType.TEXT)
        ])
    
    def test_bold_delimiter(self):
        nodes = [
            TextNode("You **bad** man!", TextType.TEXT),
            TextNode("Are you **CRAZY**?", TextType.TEXT),
        ]

        new_nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)

        self.assertEqual(new_nodes, [
            TextNode("You ", TextType.TEXT),
            TextNode("bad", TextType.BOLD),
            TextNode(" man!", TextType.TEXT),
            TextNode("Are you ", TextType.TEXT),
            TextNode("CRAZY", TextType.BOLD),
            TextNode("?", TextType.TEXT)
        ])

    def test_delimiter_with_others(self):
        nodes = [
            TextNode("This is a real bold element", TextType.BOLD),
            TextNode("This is a **fake** bold element", TextType.TEXT),
            TextNode("An image of a cat", TextType.IMAGE, url="https://www.cutecats.com/cutecat.png"),
        ]

        new_nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)

        self.assertEqual(new_nodes, [
            TextNode("This is a real bold element", TextType.BOLD),
            TextNode("This is a ", TextType.TEXT),
            TextNode("fake", TextType.BOLD),
            TextNode(" bold element", TextType.TEXT),
            TextNode("An image of a cat", TextType.IMAGE, url="https://www.cutecats.com/cutecat.png"),
        ])

if __name__ == "__main__":
    unittest.main()