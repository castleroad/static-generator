from split_nodes_delimiter import split_nodes_delimiter
from split_nodes_uri import split_nodes_image, split_nodes_link
from textnode import TextNode, TextType


def text_to_textnodes(text):
    nodes = split_nodes_link(split_nodes_image(
        [TextNode(text, TextType.TEXT)]))
    for type in TextType:
        if type == TextType.TEXT:
            continue
        nodes = split_nodes_delimiter(nodes, type.value, type)
    return nodes
