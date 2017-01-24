import pdb
from generator_sdf import *

my_robot = Model('Bob')

orig_list = ([0,2,1], [2,0,1],[0,-2,1], [-2,0,1])

box_size = [2,2,0.1]

for i,pose in enumerate(orig_list[:2]):
    my_link = Link('link-'+str(i))
    inertia = Inertial(1, pose=pose)
    visual = Visual(Geometry(Box(box_size)), pose=pose)
    collision = Collision(Geometry(Box(box_size)), pose=pose)
    my_link.add(TagList([inertia, visual, collision]))
    my_robot.add(my_link)

print('<?xml version="1.0"?>')
print('<sdf version="1.4">')
print(my_robot, end='')
print('</sdf>')

