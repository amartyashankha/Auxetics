from .base import *

class Name(AttributeBase):
    def __init__(self, name):
        super().__init__('name', name)

class XYZ(AttributeBase):
    def __init__(self, value):
        super().__init__('xyz', value)

class RPY(AttributeBase):
    def __init__(self, value):
        super().__init__('rpy', value)

class Value(AttributeBase):
    def __init__(self, value):
        super().__init__('value', value)

class Radius(AttributeBase):
    def __init__(self, value):
        super().__init__('radius', value)

class Length(AttributeBase):
    def __init__(self, value):
        super().__init__('length', value)

class File(AttributeBase):
    def __init__(self, value):
        super().__init__('filename', value)

class Scale(AttributeBase):
    def __init__(self, value):
        super().__init__('scale', value)
