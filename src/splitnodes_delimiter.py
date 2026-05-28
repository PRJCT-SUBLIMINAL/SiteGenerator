from textnode import TextType, TextNode

def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    new_list = []
    for node in old_nodes:
        if node.text_type is not TextType.TEXT:
            new_list.append(node)
            continue
        
        parts = node.text.split(delimiter)

        if len(parts) % 2 == 0:
            raise Exception("Invalid markdown syntax")

        for i in range(len(parts)):
            piece = parts[i]
            if i % 2 != 0:
                new_node = TextNode(parts[i], text_type)
                new_list.append(new_node)
            else:
                new_node = TextNode(parts[i], TextType.TEXT)
                new_list.append(new_node)
    
    return new_list