import pybullet as p
import time
import math


p.connect(p.GUI)

#p.loadURDF("urdf/plane.urdf")
p.setGravity(0,0,0)
p.setRealTimeSimulation(0)
#quadruped = p.loadURDF("r2d2.urdf")
#quadruped = p.loadURDF("urdf/first.urdf")
quadruped = p.loadSDF("sdf/first.sdf")
#quadruped = p.loadSDF("sdf/wheeled_robot.sdf")

t_end = time.time() + 10
while time.time() < t_end:
	p.stepSimulation()
