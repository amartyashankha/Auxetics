from .base import *
from .attributes import *

class Link(TagBase):
    def __init__(self, name):
        super().__init__('link')
        self.add(Name(name))

class Inertial(TagBase):
    def __init__(self, mass, inertia=[1,0,0,1,0,1], pose=None, name=None):
        super().__init__('inertial')
        self.add(Mass(mass))
        self.add(Inertia(inertia))
        self.add(Pose(pose))
        self.add(Name(name))
        
class Visual(TagBase):
    def __init__(self, geometry, pose=None, name=None):
        super().__init__('visual')
        self.add(geometry)
        self.add(Pose(pose))
        self.add(Name(name))

class Collision(TagBase):
    def __init__(self, geometry, pose=None, name=None):
        super().__init__('collision')
        self.add(geometry)
        self.add(Pose(pose))
        self.add(Name(name))

class Pose(TagSimple):
    def __init__(self, value=[]):
        default = [0, 0, 0, 0, 0, 0]
        super().__init__('pose', value+default[len(value):])

class Mass(TagSimple):
    def __init__(self, M):
        super().__init__('mass', M)

class Inertia(TagBase):
    def __init__(self, I):
        super().__init__('inertia')
        inertia_tag_list = ["ixx", "ixy", "ixz", "iyy", "iyz", "izz"]
        for tag_name,value in zip(inertia_tag_list,I):
            self.add(TagSimple(tag_name, value))

class Geometry(TagBase):
    def __init__(self, shape):
        super().__init__('geometry')
        self.add(shape)

class Box(TagBase):
    def __init__(self, size):
        super().__init__('box')
        self.add(Size(size))

class Size(TagSimple):
    def __init__(self, value):
        super().__init__('size', value)

class Cylinder(TagBase):
    def __init__(self, radius, length):
        super().__init__('cylinder')
        self.add(Radius(radius))
        self.add(Length(length))

class Sphere(TagBase):
    def __init__(self, radius, length):
        super().__init__('cylinder')
        self.add(Radius(radius))

class Mesh(TagBase):
    def __init__(self, filename, scale):
        super().__init__('cylinder')
        self.add(File(filename))
        self.add(Scale(scale))
