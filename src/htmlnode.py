
class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children if children is not None else []
        self.props = props if props is not None else {}
        
    def to_html(self):
        raise NotImplementedError("Function not implemented in HTMLNode class")

    def props_to_html(self):
        return_String = ""
        if not self.props:
            return return_String
        for prop in self.props.keys():
            return_String += f' {prop}="{self.props[prop]}"'
        return return_String

    def __repr__(self):
        string_Rep = "HTMLNode("
        add_seperator = False

        if self.tag:
            string_Rep += f"tag={repr(self.tag)}"
            add_seperator = True

        if self.value:
            if add_seperator:
                string_Rep += ", "
            string_Rep += f"value={repr(self.value)}"
            add_seperator = True
        
        if self.children:
            if add_seperator:
                string_Rep += ", "
            string_Rep += f"children={repr(self.children)}"
            add_seperator = True
        
        if self.props:
            if add_seperator:
                string_Rep += ", "
            string_Rep += f"props={repr(self.props)}"

        string_Rep += ")"
        return string_Rep


