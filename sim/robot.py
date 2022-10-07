from pyrep.objects.joint import Joint
from pyrep.const import JointMode
from pyrep.objects.dummy import Dummy
from pyrep.objects.object import Object
from pyrep.robots.end_effectors.gripper import Gripper

class Arm():
    def __init__(self, joint_names, target=None, joint_mode='ik'):
        # check that we have a valit joint mode
        if joint_mode not in ['ik', 'velocity', 'force']:
            raise Exception("joint mode not valid\n\
                    you must use one of the following:\
                    'ik', 'velocity', 'force'")
        if target is None and joint_mode == 'ik':
            raise Exception("You need to specify a target\
                    when using IK mode")
        self.joint_mode = joint_mode
        # check the integrity of the list
        try:
            joint_names[0]
        except:
            print("Joint names cannot be an empty list")
            exit(1)
        # initialize the joints
        self.joints = [Joint(j) for j in joint_names]
        # set the joint mode
        self.set_joint_mode()
        # initalize the arm target (only necessary for the IK mode)
        self.target = Dummy(target) if self.joint_mode == 'ik' else None

    # returns the position of the joint_index-th joint in radians
    def get_joint_pos(self, joint_index):
        joint = self.joints[joint_index]
        return joint.get_joint_position()

    # set joint mode to the value set on
    # the variable self.joint_mode
    def set_joint_mode(self):
        # if robot is in ik mode
        if self.joint_mode=='ik':
            for joint in self.joints:
                joint.set_joint_mode(JointMode.IK)
        # if robot is in velocity or torque mode
        else:
            self.joint_mode = 'force'
            for joint in self.joints:
                joint.set_joint_mode(JointMode.FORCE)
                joint.set_motor_enabled(True)
                joint.set_motor_locked_at_zero_velocity(True)
                joint.set_control_loop_enabled(False)

    # sets joint index i  to target velocity i
    def set_joint_velocity(self, joint_index, target_velocity):
        assert self.joint_mode=='force',\
                'set joint in velocity mode to use this function'
        self.joints[joint_index].set_joint_target_velocity(target_velocity)

class RobotGripper():
    def __init__(self, joint_names):

        pass

    def open(self):
        pass
 
    def close(self):
        pass

    def set_apperture(self):
        # Get the (thumb, wrist, index finger) angle and project the angle range to
        # the range of joint velocities from fully closed to fully opened
        pass
