from enum import Enum

class TextType(Enum):
    TEXT = "text"
    BOLD = "**text**"
    ITALIC = "_text_"
    CODE = "`text`"
    LINK = "[anchor](url)"
    IMAGE = "![alt](url)"

class TextNode:
    def __init__(self, text = None, text_type = None, url = None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, node):
        return self.text == node.text and self.text_type == node.text_type and self.url == node.url

    def __repr__(self):
        return f"{type(self).__name__}({self.text}, {self.text_type}, {self.url})"
