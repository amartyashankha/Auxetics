import pybullet as p
import time
import math


p.connect(p.GUI)

p.loadURDF("plane.urdf")
p.setGravity(0,0,-1)
p.setRealTimeSimulation(0)
#quadruped = p.loadURDF("r2d2.urdf")
quadruped = p.loadURDF("urdf/first.urdf")

#stand still
t_end = time.time() + 2
while time.time() < t_end:
	p.stepSimulation()
p.setGravity(0,0,-10)

jump_amp = 0.5

#jump
t_end = time.time() + 10
i=0
t=0
while time.time() < t_end:
	t = time.time()
	p.stepSimulation()
