import unittest
from leafnode import LeafNode
from textnode import TextType


class TestHTMLNode(unittest.TestCase):
    def test_base(self):
        node = LeafNode(tag = TextType.BOLD, value="Hello World, but in bold!")
        self.assertEqual(node.to_html(), "<b>Hello World, but in bold!</b>", "Base case test failed")

    def test_none_tag(self):
        node = LeafNode(tag = None, value="Hello, World!")
        self.assertEqual(node.to_html(), "Hello, World!", "Tag value of None test failed")

    def test_img_tag(self):
        node = LeafNode(tag=TextType.IMAGE, value="Look, an image", props={"src": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<img src="https://www.google.com" alt="Look, an image">', "Image tag test failed")
    
    def test_code_tag(self):
        node = LeafNode(tag=TextType.CODE, value="Here is some code!")
        self.assertEqual(node.to_html(), "<code>Here is some code!</code>", "Code tag test failed")
    
    def test_link_tag(self):
        node = LeafNode(tag=TextType.LINK, value="Click me!", props={"href": "https://www.example.com"})
        self.assertEqual(node.to_html(), "<a href=\"https://www.example.com\">Click me!</a>", "hyperlink tag test failed")

    def test_none_value(self):
        node = LeafNode(tag=None, value=None)
        with self.assertRaises(ValueError, msg="LeafNode not having a value test case failed"):
            node.to_html()

    

        

if __name__ == "__main__":
    unittest.main()