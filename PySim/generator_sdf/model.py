from .base import *
from .attributes import *

class Model(TagBase):
    def __init__(self, name):
        super().__init__('model')
        self.add(Name(name))
