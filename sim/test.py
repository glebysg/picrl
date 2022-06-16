from pyrep import PyRep
from pyrep.objects.joint import Joint
import time

pr = PyRep()
# Launch the application with a scene file in headless mode
pr.launch('../models/assembly_joints.ttt', headless=False)
pr.start()  # Start the simulation

#######################
# initialize          #
#######################
# Todo: make into a robot class
c_shoulder_1 = Joint("Joint10_1")
c_shoulder_2 = Joint("Joint10_2")
c_shoulder_3 = Joint("Joint10_3")
c_elbow = Joint("Joint0")

c_shoulder_2.set_joint_position(50)
c_elbow.set_joint_position(-40)
pr.step()

time.sleep(3)

pr.stop()  # Stop the simulation
pr.shutdown()  # Close the application
