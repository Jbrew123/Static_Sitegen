from enum import Enum

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"



class TextNode():
    def __init__(self, text, text_type, url):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, textnode_1, textnode_2):
        if textnode_1.text != textnode_2.text:
            return False
        
        if textnode_1.text_type != textnode_2.text_type:
            return False
        
        if textnode_1.url != textnode_2.url:
            return False
        
        return True


    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
    
