import unittest

from textnode import TextNode, TextType
from split_nodes_delimiter import split_nodes_delimiter

class TestSplitNodeDelimiter(unittest.TestCase):
    def test_text_to_code(self):
        node = TextNode("This is a text node `with code`", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(
            new_nodes, [
                TextNode("This is a text node ", TextType.TEXT),
                TextNode("with code", TextType.CODE),
            ]
        )

    def test_text_to_italic(self):
        node = TextNode("This is a text node _with italic_ and more text", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertEqual(
            new_nodes, [
                TextNode("This is a text node ", TextType.TEXT),
                TextNode("with italic", TextType.ITALIC),
                TextNode(" and more text", TextType.TEXT),
            ]
        )

    def test_text_to_bold(self):
        node = TextNode("**Some bold text** and some more text", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(
            new_nodes, [
                TextNode("Some bold text", TextType.BOLD),
                TextNode(" and some more text", TextType.TEXT),
            ]
        )
    
    def test_code_to_italic_fails(self):
        node = TextNode("This is a code node try to convert to _italic_", TextType.CODE)
        new_nodes = split_nodes_delimiter([node], "`", TextType.ITALIC)
        self.assertEqual(new_nodes, [node])

    def test_unmatched_italic_delimiter_exception(self):
        node = TextNode("This is a text node _with unmatched italic delimiter", TextType.TEXT)
        with self.assertRaises(Exception):
            split_nodes_delimiter([node], "_", TextType.ITALIC)

    def test_unmatched_bold_delimiter_at_end_of_text_exception(self):
        node = TextNode("This is a text node with unmatched bold delimiter at the end**", TextType.TEXT)
        with self.assertRaises(Exception):
            split_nodes_delimiter([node], "**", TextType.BOLD)

    def test_multiple_nodes_split_succesfully(self):
        nodes = [
            TextNode("**Bold text** in regular text", TextType.TEXT),
            TextNode("Some regular and _italic_ text", TextType.TEXT),
            TextNode("Some regular with **bold** convert `code snippet`", TextType.TEXT),
        ]
        new_nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
        self.assertEqual(new_nodes, [
            TextNode("Bold text", TextType.BOLD),
            TextNode(" in regular text", TextType.TEXT),
            TextNode("Some regular and _italic_ text", TextType.TEXT),
            TextNode("Some regular with ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" convert `code snippet`", TextType.TEXT),
        ])

if __name__ == "__main__":
    unittest.main()
