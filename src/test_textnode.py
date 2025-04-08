import unittest
from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
        
        node3 = TextNode("Changing not equal", TextType.ITALIC)
        self.assertNotEqual(node, node3)

        node4 = TextNode("This is a text node", TextType.TEXT)
        self.assertNotEqual(node, node4)

        node5 = TextNode("This is an image text node", TextType.IMAGE, "www.google.com")
        node6 = TextNode("This is an image text node", TextType.IMAGE, "www.google.com")
        node7 = TextNode("This is an image text node", TextType.IMAGE)

        self.assertEqual(node5, node6)
        self.assertNotEqual(node5, node7)


if __name__ == "__main__":
    unittest.main()
