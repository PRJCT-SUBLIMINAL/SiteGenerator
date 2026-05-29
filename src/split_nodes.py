from textnode import TextNode, TextType
from extract_markdown import extract_markdown_images, extract_markdown_links

def split_nodes_bold(old_nodes: list[TextNode]) -> list[TextNode]:
    new_list = []
    for node in old_nodes:
        if node.text_type is not TextType.TEXT:
            new_list.append(node)
            continue

def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    new_list = []
    for node in old_nodes:
        original_text = node.text
        if node.text_type is not TextType.TEXT:
            new_list.append(node)
            continue

        images = extract_markdown_images(original_text)
        if len(images) == 0:
            new_list.append(node)
            continue
        
        for image in images:
            sections = original_text.split(f"![{image[0]}]({image[1]})", 1)
            original_text = sections[1]

            if sections[0] != "":
                new_list.append(TextNode(sections[0], TextType.TEXT))

            new_list.append(TextNode(image[0], TextType.IMAGE, image[1]))

        if original_text != "":
            new_list.append(TextNode(original_text, TextType.TEXT))

    return new_list

def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    new_list = []
    for node in old_nodes:
        original_text = node.text
        if node.text_type is not TextType.TEXT:
            new_list.append(node)
            continue
        
        links = extract_markdown_links(original_text)
        if len(links) == 0:
            new_list.append(node)
            continue
        
        for link in links:
            sections = original_text.split(f"[{link[0]}]({link[1]})")
            original_text = sections[1]

            if sections[0] != "":
                new_list.append(TextNode(sections[0], TextType.TEXT))
            
            new_list.append(TextNode(link[0], TextType.LINK, link[1]))

        if original_text != "":
            new_list.append(TextNode(original_text, TextType.TEXT))
    
    return new_list