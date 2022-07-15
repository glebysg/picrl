from pyrep import PyRep
from pyrep.objects.joint import Joint
from pyrep.objects.shape import Shape
from pyrep.objects.dummy import Dummy
from robot import Arm
import time
import math
import random

class Humanoid():
    def __init__(self, name_index=['',''], mode='velocity'):
        joint_names_r = ["Joint20_2", "Joint20_3", "Joint20_1",
                        "Elbow1", "Joint22", "Joint23"]
        joint_names_l = joint_names_r[:] 
        joint_names_l = [j_name+name_index[0] for j_name in joint_names_l]
        joint_names_r = [j_name+name_index[1] for j_name in joint_names_r]
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
        self.pr.launch('../models/veocity test2.ttt', headless=False)
        self.pr.start()  # Start the simulation
        self.collaborator = Humanoid(name_index=['#0',''], mode='velocity')

    def step(self):
        self.pr.step()

    def reset(self):
        pass

    def close(self):
        self.pr.stop()
        self.pr.shutdown()

if __name__ == "__main__":
    env = HumanoidEnv()
    r_direction = [1, -1, 1, 1, -1, -1]
    l_direction = [1, 1, 1, 1, 1, 1]
    r_goal = [130, -40, 0, 75,-15, -15]
    l_goal = [120, 20, 30, 50, 20, 0]
    for joint_index in range(len(env.collaborator.right.joints)):
        step = 0.1 if joint_index > 2 else 0.2
        env.collaborator.right.set_joint_velocity(joint_index, r_direction[joint_index]*step)
        env.collaborator.left.set_joint_velocity(joint_index, l_direction[joint_index]*step)
    
    for i in range(1000):
        env.step()
        for joint_index in range(len(env.collaborator.right.joints)):
            pos_r = math.degrees(env.collaborator.right.get_joint_pos(joint_index))
            # if we reached the goal at joint_index-th joint in the RIGHT arm
            if (r_direction[joint_index] == -1 and pos_r<= r_goal[joint_index]) or\
               (r_direction[joint_index] == 1 and pos_r >= r_goal[joint_index]):
                env.collaborator.right.set_joint_velocity(joint_index, 0)
            # if we reached the goal at joint_index-th joint in the LEFT arm
            pos_l = math.degrees(env.collaborator.left.get_joint_pos(joint_index))
            if (l_direction[joint_index] == -1 and pos_l<= l_goal[joint_index]) or\
               (l_direction[joint_index] == 1 and pos_l >= l_goal[joint_index]):
                env.collaborator.left.set_joint_velocity(joint_index, 0)
    env.close()
