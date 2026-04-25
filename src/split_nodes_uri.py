from textnode import TextType, TextNode
from extract_markdown import extract_markdown_images, extract_markdown_links


def split_nodes_link(nodes):
    new_nodes = []
    for n in nodes:
        if n.text_type is not TextType.TEXT:
            new_nodes.append(n)
            continue
        links = extract_markdown_links(n.text)
        if len(links) == 0:
            new_nodes.append(n)
            continue
        l, i, j = 0, 0, 0
        for j in range(len(n.text)):
            if n.text[j] == "[" and n.text[j-1] == " ":
                new_nodes.append(TextNode(n.text[i:j], TextType.TEXT))
                new_nodes.append(
                    TextNode(links[l][0], TextType.LINK, links[l][1]))
                while n.text[j] != ")":
                    j += 1
                j += 1
                i = j
                l += 1
                if l == len(links) and i < len(n.text):
                    new_nodes.append(TextNode(n.text[i:], TextType.TEXT))
                    break
    return new_nodes


def split_nodes_image(nodes):
    new_nodes = []
    for n in nodes:
        if n.text_type is not TextType.TEXT:
            new_nodes.append(n)
            continue
        images = extract_markdown_images(n.text)
        if len(images) == 0:
            new_nodes.append(n)
            continue
        im, i, j = 0, 0, 0
        for j in range(len(n.text)):
            if n.text[j] == "!" and n.text[j+1] == "[":
                new_nodes.append(TextNode(n.text[i:j], TextType.TEXT))
                new_nodes.append(
                    TextNode(images[im][0], TextType.IMAGE, images[im][1]))
                while n.text[j] != ")":
                    j += 1
                j += 1
                i = j
                im += 1
                if im == len(images) and i < len(n.text):
                    new_nodes.append(TextNode(n.text[i:], TextType.TEXT))
                    break
    return new_nodes
