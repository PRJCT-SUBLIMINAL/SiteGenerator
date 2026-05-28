class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        if self.props is None or self.props == {}:
            return ""
        
        props_string = ""

        for prop in self.props:
            props_string += f' {prop}="{self.props[prop]}"'
        
        return props_string
    
    def __repr__(self):
        return f'HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})'

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag=tag, value=value, props=props, children=None)

    def to_html(self):
        if self.value is None:
            raise ValueError()
        
        if self.tag is None:
            return f'{self.value}'
        
        return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'
    
    def __repr__(self):
        return f'LeafNode({self.tag}, {self.value}, {self.props})'

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, children=children, props=props)

    def to_html(self):
        if self.tag is None:
            raise ValueError()
        
        if self.children is None:
            raise ValueError("Missing children in initialization. Children are not optional for a parent node.")

        htmlstring = ""

        for child in self.children:
            htmlstring += child.to_html()
        
        return f'<{self.tag}{self.props_to_html()}>{htmlstring}</{self.tag}>'