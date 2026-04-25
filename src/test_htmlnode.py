import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode(
            props={"href": "https://www.google.com", "target": "_blank"}
        )
        repr = node.props_to_html()
        self.assertEqual(
            repr, " href=\"https://www.google.com\" target=\"_blank\"")


if __name__ == "__main__":
    unittest.main()
