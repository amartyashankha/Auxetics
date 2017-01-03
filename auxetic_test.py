from dxfwrite import DXFEngine as dxf
import math
import numpy as np

mirror = False
grid_y = 7
grid_x = 7

offset = 30
bend_width = 10

grid_spacing = 120

angle = 15 

flag = False

#stroke = svgwrite.rgb(10, 10, 10, '%')

drawing = dxf.drawing('auxetic_test.dxf')
drawing.add(dxf.rectangle(insert=(-1*bend_width, -1*bend_width),
                          width=grid_spacing *(grid_x)+2*bend_width ,
                          height=grid_spacing *(grid_y)+2*bend_width ))
#dwg.viewbox(width=grid_spacing*(grid_x), height=grid_spacing*(grid_y))

def print_box(grid_x, grid_y, offset, angle, mirror,
              bend_width=5,
              rng=grid_spacing,
              hinge=0.07):
    x_min = grid_x*rng
    y_min = grid_y*rng
    ref = np.array([x_min, y_min])

    if angle < 0.1 and not flag:
        return
    top_left = (np.array([bend_width, 0]), np.array([offset, offset+angle]))
    bottom_right = (np.array([rng-bend_width, rng]), np.array([rng-offset, rng-(offset+angle)]))
    top_right = (np.array([rng, bend_width]), np.array([rng-(offset+angle), offset]))
    bottom_left = (np.array([0, rng-bend_width]), np.array([offset+angle, rng-offset]))

    lines = [top_left, top_right, bottom_right, bottom_left]

    lines = [line+ref for line in lines]

    if mirror:
        lines = [[point[::-1] for point in line] for line in lines]

    for l in lines:
        line = dxf.line(l[0], l[1], color=7)
        drawing.add(line)

    square = []
    for i in range(len(lines)):
        line = dxf.line(lines[i][1], (hinge*lines[i][1]+lines[i-1][1])/(1+hinge), color=7)
        square.append(lines[i][1])
        drawing.add(line)

    square.reverse()
#    drawing.add(dxf.polyline(square, color=3))


k = 0.2
c = 6

for gx in range(grid_x):
    for gy in range(grid_y):
        x = gx - grid_x/2
        y = gy - grid_y/2
        r = math.sqrt(x*x+y*y)
        sec = math.sqrt(1 + (-c*math.exp(-k*r*r)*k*r)**2)
        curr_angle = grid_spacing*0.5*(math.sqrt(sec)-1)
        if x == 0 and y == 0:
            flag = True
        else:
            flag = False
        print_box(gx, gy, offset, angle, mirror=((gx+gy)%2==0), bend_width=bend_width)
        print round(curr_angle, 1),
    print ''

drawing.save()
