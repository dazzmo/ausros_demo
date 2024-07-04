import casadi
import numpy as np

import pinocchio as pin
import pinocchio.casadi as cpin

import time

from example_robot_data import load

robot = load('ur3')

# Select the default configuration for the robot.
q0 = robot.q0
# OPTIONAL - Instead, choose a random configuration within the configuration space of the model
# q0 = pin.randomConfiguration(robot.model)

## visualise the robot
import meshcat
from pinocchio.visualize import MeshcatVisualizer
viz = MeshcatVisualizer(robot.model, robot.collision_model, robot.visual_model)
# Start a new MeshCat server and client.
viz.initViewer(open=True)
# Load the robot in the viewer.
viz.loadViewerModel()
# Display the robot with the initial state q0
viz.display(q0)

# Display reference as a transparent red model
viz_ref = MeshcatVisualizer(robot.model, robot.collision_model, robot.visual_model)
viz_ref.initViewer(viz.viewer)
viz_ref.loadViewerModel(rootNodeName="reference", color=[1.0, 0.0, 0.0, 0.1])

# small time window for loading the model 
# if meshcat does not visualise the robot properly, augment the time
# it can be removed in most cases
time.sleep(0.2) 