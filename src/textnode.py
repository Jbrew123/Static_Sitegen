from enum import Enum

class TextType(Enum):
    TEXT = "text"
    BOLD = "b"
    ITALIC = "i"
    CODE = "code"
    LINK = "a"
    IMAGE = "img"



class TextNode():
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, textnode_2):
        if self.text != textnode_2.text:
            return False
        
        if self.text_type != textnode_2.text_type:
            return False
        
        if self.url != textnode_2.url:
            return False
        
        return True


    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
    
