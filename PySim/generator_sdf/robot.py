from .base import *
from .attributes import *

class Robot(TagBase):
    def __init__(self, name):
        super().__init__('robot')
        self.add(Name(name))
