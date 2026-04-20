from textnode import TextType
from leafnode import LeafNode

def text_to_html(node):
    match node.text_type:
        case TextType.TEXT:
            return LeafNode(None, node.text)
        case TextType.BOLD:
            return LeafNode("b", node.text)
        case TextType.ITALIC:
            return LeafNode("i", node.text)
        case TextType.CODE:
            return LeafNode("code", node.text)
        case TextType.LINK:
            return LeafNode("a", node.text, None, {"href": node.url})
        case TextType.IMAGE:
            return LeafNode("img", "", None, {"src": node.url, "alt": node.text})
        case _:
            raise Exception("Unknown node type")
