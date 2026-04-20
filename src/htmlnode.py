class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("Should be implemented by subclass")

    def props_to_html(self):
        html = ""
        if not self.props:
            return html

        for p in self.props:
            html += f" {p}=\"{self.props[p]}\""

        return html

    def __repr__(self):
        return f"{type(self).__name__} Tag {self.tag} Value = {self.value} Props = {self.props} Children count = {0 if not self.children else len(self.children)}"
