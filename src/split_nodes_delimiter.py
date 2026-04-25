from textnode import TextType, TextNode


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for n in old_nodes:
        if n.text_type is not TextType.TEXT:
            new_nodes.append(n)
            continue
        sections = n.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise Exception("No matching closing delimiter have been found")

        for i, section in enumerate(sections):
            if section == "":
                continue
            if i % 2 == 0:
                new_nodes.append(TextNode(section, TextType.TEXT))
            else:
                new_nodes.append(TextNode(section, text_type))
    return new_nodes
