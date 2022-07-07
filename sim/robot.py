from pyrep.objects.joint import Joint
from pyrep.const import JointMode
from pyrep.objects.dummy import Dummy
from pyrep.objects.object import Object

class Arm():
    def __init__(self, joint_names, target=None, joint_mode='ik'):
        # check that we have a valit joint mode
        if joint_mode not in ['ik', 'velocity', 'force']:
            raise Exception("joint mode not valid\n\
                    you must use one of the following:\
                    'ik', 'velocity', 'force'")
        self.joint_mode = joint_mode
        # set the joint mode
        se
        # check the integrity of the list
        try:
            joint_names[0]
        except:
            print("Joint names cannot be an empty list")
            exit(1)
        # initialize the joints
        self.joints = [Joint(j) for j in joint_names]
        # initalize the arm target (only necessary for the IK mode)
        self.target = Dummy(target) if self.joint_mode == 'ik' else None

    # set joint mode to the value set on
    # the variable self.joint_mode
    def set_joint_mode(self):
        # if robot is in ik mode
        if self.joint_mode=='ik':
            for joint in self.joints:
                joint.set_joint_mode(JointMode.IK)
        # if robot is in velocity or torque mode
        else:
            self.jointmode = 'force'
            for joint in self.joints:
                joint.set_joint_mode(JointMode.FORCE)
                joint.set_motor_enabled(True)
                joint.set_motor_locked_at_zero_velocity(False)
                joint.set_control_loop_enabled(False)

    # sets joint index i  to target velocity i
    def set_joint_velocity(self, joint_index, target_velocity):
        assert self.jointmode=='force',\
                'set joint in velocity mode to use this function'
        self.joints[joint_n].set_joint_target_velocity(target_velocity)
