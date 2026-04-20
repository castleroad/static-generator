from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if not self.tag:
            raise ValueError("Parent node should have a tag")

        children = ""
        for c in self.children:
            children += c.to_html()

        return f"<{self.tag}{self.props_to_html()}>{children}</{self.tag}>"

    def __repr__(self):
        return f"{type(self).__name__} Tag {self.tag} Props = {self.props} Children count = {0 if not self.children else len(self.children)}"
