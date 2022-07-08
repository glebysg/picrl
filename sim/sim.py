from pyrep import PyRep
from pyrep.objects.joint import Joint
from pyrep.objects.shape import Shape
from pyrep.objects.dummy import Dummy
from robot import Arm
import time
import math
import random

class Humanoid():
    def __init__(self, name_index="#5", mode='velocity'):
        joint_names_r = ["Joint10_1", "Joint10_2", "Joint10_3",
                        "Joint0", "Joint2", "Joint16"]
        joint_names_l = ["Joint9_1", "Joint9_2", "Joint9_3",
                        "Joint", "Joint1", "Joint15"]
        joint_names_l = [j_name+name_index for j_name in joint_names_l]
        joint_names_r = [j_name+name_index for j_name in joint_names_r]
        self.left = Arm(joint_names_l, None, mode)
        self.right = Arm(joint_names_r, None, mode)

        # GRIPPER TODO put in the class
        # c_indexthumb_1=Joint("JacoHand_fingers12_motor1#3")
        # c_indexthumb_2=Joint("JacoHand_fingers12_motor2#3")
        # c_middle_1=Joint("JacoHand_finger3_motor1#3")
        # c_middle_2=Joint("JacoHand_finger3_motor2#3")
        # c_hand_shape = Shape("Rectangle2")
        # c_arm = [c_shoulder_2,c_shoulder_3,c_shoulder_1,c_elbow, c_wrist_2, c_wrist_16]

class HumanoidEnv():
    def __init__(self):
        self.pr = PyRep()
        # Launch the application with a scene file in headless mode
        self.pr.launch('../models/assembly_joints_human.ttt', headless=False)
        self.pr.start()  # Start the simulation
        self.collaborator = Humanoid(name_index='#5', mode='velocity')
        for joint_index in range(len(self.collaborator.right.joints)):
            self.collaborator.right.set_joint_velocity(joint_index, 0.1)

    def step(self):
        self.pr.step()

    def reset(self):
        pass

    def close(self):
        self.pr.stop()
        self.pr.shutdown()

if __name__ == "__main__":
    env = HumanoidEnv()
    for i in range(100):
        env.step()
        for joint_index in range(len(env.collaborator.right.joints)):
            env.collaborator.right.set_joint_velocity(joint_index, 0.1)
    env.close()
