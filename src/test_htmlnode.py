import unittest
from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode(tag="tag_example", value="value_example", children=[1, 2, 3], props={"href": "www.example.com"})       
        assert repr(node) == "HTMLNode(tag='tag_example', value='value_example', children=[1, 2, 3], props={'href': 'www.example.com'})", "repr output mismatch on test case 1"
        
        
    
    def test_no_tag(self):
        node2 = HTMLNode(value="value_example", children=[1, 2, 3], props={"href": "www.example.com"})
        assert repr(node2) == "HTMLNode(value='value_example', children=[1, 2, 3], props={'href': 'www.example.com'})", "repr output mismatch on test case 2"

    def test_no_value(self):
        node3 = HTMLNode(tag="tag_example", children=[1, 2, 3], props={"href": "www.example.com"})
        assert repr(node3) == "HTMLNode(tag='tag_example', children=[1, 2, 3], props={'href': 'www.example.com'})", "repr output mismatch on test case 3"

    def test_no_children(self):
        node4 = HTMLNode(tag="tag_example", value="value_example", props={"href": "www.example.com"})
        assert repr(node4) == "HTMLNode(tag='tag_example', value='value_example', props={'href': 'www.example.com'})", "repr output mismatch on test case 4"

    def test_no_props(self):
        node5 = HTMLNode(tag="tag_example", value="value_example", children=[1, 2, 3])
        assert repr(node5) == "HTMLNode(tag='tag_example', value='value_example', children=[1, 2, 3])", "repr output mismatch on test case 5"

    def test_empty_htmlnode(self):
        node6 = HTMLNode()
        assert repr(node6) == "HTMLNode()", "repr output mismatch on test case 6"

    def test_complex_props(self):
        node7 = HTMLNode(props={"href": "www.example.com", "target": "_blank"})
        assert node7.props_to_html() == ' href="www.example.com" target="_blank"', "Props formatting failed!"

    def test_to_html_raises(self):
        node = HTMLNode()
        with self.assertRaises(NotImplementedError):
            node.to_html()

    def test_props_to_html_empty(self):
        node = HTMLNode()
        self.assertEqual(node.props_to_html(), "", "props_to_html() did not return empty string when props was empty/None")

if __name__ == "__main__":
    unittest.main()