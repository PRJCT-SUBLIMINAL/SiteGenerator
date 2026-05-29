from enum import Enum
from htmlnode import HTMLNode, ParentNode
from textnode import TextNode, TextType, text_node_to_html_node
from inline_markdown import text_to_textnodes

def markdown_to_blocks(markdown):
    new_markdown = markdown.split("\n\n")
    markdown_list = []
    for markdown_text in new_markdown:
        if markdown_text != "":
            markdown_list.append(markdown_text.strip())
    return markdown_list

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_blocktype(markdown):
    if markdown.startswith(("###### ", "##### ", "#### ", "### ", "## ", "# ")):
        return BlockType.HEADING
    elif markdown.startswith(("```\n")) and markdown.endswith(("```")):
        return BlockType.CODE
    elif markdown.startswith((">")):
        split_markdown = markdown.split("\n")
        for markdown_line in split_markdown:
            if not markdown_line.startswith(">"):
                return BlockType.PARAGRAPH
        return BlockType.QUOTE
    elif markdown.startswith(("- ")):
        split_markdown = markdown.split("\n")
        for markdown_line in split_markdown:
            if not markdown_line.startswith("- "):
                return BlockType.PARAGRAPH
        return BlockType.UNORDERED_LIST
    elif markdown.startswith(("1. ")):
        split_markdown = markdown.split("\n")
        for i in range(0, len(split_markdown)):
            if not split_markdown[i].startswith(f'{i+1}. '):
                return BlockType.PARAGRAPH
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        children.append(html_node)
    return children

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    nodes = []
    for block in blocks:
        block_type = block_to_blocktype(block)
        match(block_type):
            case BlockType.PARAGRAPH:
                paragraph = " ".join(block.split("\n"))
                block_children = text_to_children(paragraph)
                node = ParentNode(tag="p", children=block_children)
                nodes.append(node)
                continue
            
            case BlockType.HEADING:
                hashes = ""
                for char in block:
                    if char == " ":
                        break
                    if char == "#":
                        hashes += "#"
                if len(hashes) >= 1 and len(hashes) <= 6:
                    new_block = block[len(hashes) + 1:]
                    block_children = text_to_children(new_block)
                    node = ParentNode(tag=f"h{len(hashes)}", children=block_children)
                    nodes.append(node)

            case BlockType.CODE:
                text = block[4:-3]
                text_node = text_node_to_html_node(TextNode(text, TextType.TEXT))
                code_node = ParentNode(tag="code", children=[text_node])
                node = ParentNode(tag="pre", children=[code_node])
                nodes.append(node)

            case BlockType.QUOTE:
                lines = []
                new_blocks = block.split("\n")
                for new_block in new_blocks:
                    lines.append(new_block.lstrip("> ").strip())
                new_block = " ".join(lines)
                block_children = text_to_children(new_block)
                node = ParentNode(tag="blockquote", children=block_children)
                nodes.append(node)

            case BlockType.UNORDERED_LIST:
                block_children = []
                new_blocks = block.split("\n")
                for new_block in new_blocks:
                    text = new_block[2:]
                    list_children = text_to_children(text)
                    li_node = ParentNode(tag="li", children=list_children)
                    block_children.append(li_node)
                ul_node = ParentNode(tag="ul", children=block_children)
                nodes.append(ul_node)

            case BlockType.ORDERED_LIST:
                block_children = []
                new_blocks = block.split("\n")
                for new_block in new_blocks:
                    text = new_block[3:]
                    list_children = text_to_children(text)
                    li_node = ParentNode(tag="li", children=list_children)
                    block_children.append(li_node)
                ol_node = ParentNode(tag="ol", children=block_children)
                nodes.append(ol_node)
    
    parent_node = ParentNode(tag="div", children=nodes)
    return parent_node