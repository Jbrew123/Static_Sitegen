from htmlnode import HTMLNode
from textnode import TextType

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)
        
    def to_html(self):
        if self.value == None:
            raise ValueError("LeafNode does not have a value")
        
        if self.tag == None:
            return f"{self.value}"
        
        if self.tag == TextType.IMAGE:
            return f'<img{self.props_to_html()} alt="{self.value}">'

        return f"<{self.tag.value}{self.props_to_html()}>{self.value}</{self.tag.value}>"