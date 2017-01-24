from .base import *
from .attributes import *

class Link(TagBase):
    def __init__(self, name):
        super().__init__('link')
        self.add(Name(name))

class Inertial(TagBase):
    def __init__(self, mass, inertia=[1,0,0,1,0,1], origin=None, name=None):
        super().__init__('inertial')
        self.add(Mass(mass))
        self.add(Inertia(inertia))
        self.add(Origin(origin))
        self.add(Name(name))
        
class Visual(TagBase):
    def __init__(self, geometry, origin=None, name=None):
        super().__init__('visual')
        self.add(geometry)
        self.add(Origin(origin))
        self.add(Name(name))

class Collision(TagBase):
    def __init__(self, geometry, origin=None, name=None):
        super().__init__('collision')
        self.add(geometry)
        self.add(Origin(origin))
        self.add(Name(name))

class Origin(TagBase):
    def __init__(self, xyz=None, rpy=None):
        super().__init__('origin')
        if xyz is not None:
            self.add(XYZ(xyz))
        if rpy is not None:
            self.add(RPY(rpy))

class Mass(TagBase):
    def __init__(self, M):
        super().__init__('mass')
        self.add(Value(M))

class Inertia(TagBase):
    def __init__(self, I):
        super().__init__('inertia')
        inertia_attribute_list = ["ixx", "ixy", "ixz", "iyy", "iyz", "izz"]
        for attribute,value in zip(inertia_attribute_list,I):
            self.add(AttributeBase(attribute, value))

class Geometry(TagBase):
    def __init__(self, shape):
        super().__init__('geometry')
        self.add(shape)

class Box(TagBase):
    def __init__(self, size):
        super().__init__('box')
        self.add(Size(size))

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
