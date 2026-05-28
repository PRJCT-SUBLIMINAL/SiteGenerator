from textnode import TextNode, TextType, text_node_to_html_node
from split_nodes import *
from splitnodes_delimiter import split_nodes_delimiter

def text_to_textnodes(text):
    text_node = TextNode(text, TextType.TEXT)
    nodes = split_nodes_delimiter([text_node], "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes