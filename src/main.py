from textnode import TextNode, TextType

def Main():
    text_node = TextNode("This is some anchor text", TextType.TEXT_LINK, "https://www.boot.dev")
    print(text_node)

Main()