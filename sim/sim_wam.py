from pyrep import PyRep
from pyrep.objects.joint import Joint
from pyrep.objects.shape import Shape
from pyrep.objects.dummy import Dummy
from robot import Arm, Gripper
import time
import math
import random

class WamRobot():
    def __init__(self, robot_index='', gripper_index='', mode='velocity'):
        joint_names = [ "wam_base_yaw_joint", "wam_shoulder_pitch_joint",
                    "wam_shoulder_yaw_joint", "wam_elbow_pitch_joint",
                    "wam_wrist_yaw_joint", "wam_wrist_pitch_joint",
                    "wam_palm_yaw_joint"]
        target_name = "wam_target"
        joint_names = [j_name+robot_index for j_name in joint_names]
        self.arm = Arm(joint_names,target_name, mode)
        gripper_names = []
        self.gripper = None

class Humanoid():
    def __init__(self, name_index=['',''], mode='velocity'):
        joint_names_r = ["Joint20_2", "Joint20_3", "Joint20_1",
                        "Elbow1", "Joint22", "Joint23"]
        joint_names_l = joint_names_r[:]
        joint_names_l = [j_name+name_index[0] for j_name in joint_names_l]
        joint_names_r = [j_name+name_index[1] for j_name in joint_names_r]
        self.left = Arm(joint_names_l, None, mode)
        self.right = Arm(joint_names_r, None, mode)

class WamEnv():
    def __init__(self):
        self.pr = PyRep()
        # Launch the application with a scene file in headless mode
        self.pr.launch('../models/wam_rl.ttt', headless=False)
        self.pr.start()  # Start the simulation
        # self.robot = WamRobot(robot_index='',gripper_index='', mode='velocity')
        # self.collaborator= Humanoid(name_index=['#0',''], mode='velocity')
        self.robot = WamRobot(robot_index='',gripper_index='', mode='ik')
        self.collaborator= Humanoid(name_index=['#0',''], mode='velocity')

    def step(self):
        self.pr.step()

    def reset(self):
        pass

    def close(self):
        self.pr.stop()
        self.pr.shutdown()

if __name__ == "__main__":
    env = WamEnv()
    ## WAM
    # step = 0.1
    # for joint_index in range(len(env.robot.arm.joints)):
        # env.robot.arm.set_joint_velocity(joint_index,step)

    ## Colaborator
    for joint_index in range(len(env.collaborator.right.joints)):
        step = 0.1 if joint_index > 2 else 0.2
        env.collaborator.right.set_joint_velocity(joint_index, step)
        env.collaborator.left.set_joint_velocity(joint_index, step)

    for i in range(1000):
        env.robot.arm.target.set_position(
                [0,0,0.01],relative_to=env.robot.arm.target)
        env.step()
    env.close()
