from dxfwrite import DXFEngine as dxf
import numpy as np

mirror = False
grid_y = 1
grid_x = 8

grid_spacing = 120
gap = 10

#stroke = svgwrite.rgb(10, 10, 10, '%')

drawing = dxf.drawing('angle_test.dxf')
#drawing.viewbox(width=grid_spacing*(grid_x), height=grid_spacing*(grid_y))

def print_angle(grid_x, grid_y,
                hinge=10):
    x_min = grid_x*grid_spacing
    y_min = grid_y*grid_spacing
    ref = np.array([x_min, y_min])

    left = np.array([gap, grid_spacing/2])
    right = np.array([grid_spacing-gap, grid_spacing/2])
    bottom = np.array([grid_spacing/2, grid_spacing-gap])
    top = np.array([grid_spacing/2, gap])

    top_left = (top, left)
    top_right = (top, right)
    bottom_left = (bottom, left)
    bottom_right = (bottom, right)
    top_bottom = (top+np.array([0, hinge]), bottom)

    lines = [top_bottom, top_left, top_right, bottom_right, bottom_left]

    lines = [line+ref for line in lines]

    for l in lines:
        line = dxf.line(l[0], l[1], color=7) 
        drawing.add(line)

hinge = 3

for gx in range(grid_x):
    print_angle(gx, 0, int(hinge))
    hinge = hinge*1.3

drawing.save()
