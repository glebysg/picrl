from pyrep import PyRep
from pyrep.objects.joint import Joint
from pyrep.objects.shape import Shape
from pyrep.objects.dummy import Dummy
import time
import math
import random

pr = PyRep()
# Launch the application with a scene file in headless mode
pr.launch('../models/assembly_joints_test.ttt', headless=False)
pr.start()  # Start the simulation

#######################
# initialize          #
#######################
# Todo: make into a robot class
step = 0.05
##### COLLABORATOR #############
c_shoulder_1 = Joint("Joint10_1")
c_shoulder_2 = Joint("Joint10_2")
c_shoulder_3 = Joint("Joint10_3")
c_elbow = Joint("Joint0")
c_wrist_2 = Joint("Joint2")
c_wrist_16 = Joint("Joint16")
c_indexthumb_1=Joint("JacoHand_fingers12_motor1#3")
c_indexthumb_2=Joint("JacoHand_fingers12_motor2#3")
c_middle_1=Joint("JacoHand_finger3_motor1#3")
c_middle_2=Joint("JacoHand_finger3_motor2#3")
c_hand_shape = Shape("Rectangle2")
c_arm = [c_shoulder_2,c_shoulder_3,c_shoulder_1,c_elbow, c_wrist_2, c_wrist_16]
c_hand = [c_indexthumb_1, c_indexthumb_2, c_middle_1, c_middle_2]

##### USER #############
u_shoulder_1 = Joint("Joint10_1#0")
u_shoulder_2 = Joint("Joint10_2#0")
u_shoulder_3 = Joint("Joint10_3#0")
u_elbow = Joint("Joint0#0")
u_wrist_2 = Joint("Joint2#0")
u_wrist_16 = Joint("Joint16#0")
u_indexthumb_1=Joint("JacoHand_fingers12_motor1")
u_indexthumb_2=Joint("JacoHand_fingers12_motor2")
u_middle_1=Joint("JacoHand_finger3_motor1")
u_middle_2=Joint("JacoHand_finger3_motor2")
u_hand_shape = Shape("Rectangle2#0")
u_arm = [u_shoulder_2,u_shoulder_3,u_shoulder_1,u_elbow, u_wrist_2, u_wrist_16]
u_hand = [u_indexthumb_1, u_indexthumb_2, u_middle_1, u_middle_2]

s_shoulder_1 = Joint("Joint9_1#0")
s_shoulder_2 = Joint("Joint9_2#0")
s_shoulder_3 = Joint("Joint9_3#0")
s_elbow = Joint("Joint#0")
s_wrist_2 = Joint("Joint1#0")
s_wrist_16 = Joint("Joint15#0")
s_indexthumb_1=Joint("JacoHand_fingers12_motor1#0")
s_indexthumb_2=Joint("JacoHand_fingers12_motor2#0")
s_middle_1=Joint("JacoHand_finger3_motor1#0")
s_middle_2=Joint("JacoHand_finger3_motor2#0")
s_hand_shape = Shape("Rectangle1#0")
s_arm = [s_shoulder_2,s_shoulder_3,s_shoulder_1,s_elbow, s_wrist_2, s_wrist_16]
s_hand = [s_indexthumb_1, s_indexthumb_2, s_middle_1, s_middle_2]



##### OBJECTS  #############
tweezers = Shape("Tweezers")
electronic = Shape("Shape0")
glass = Shape("Shape2")
torch = Dummy("WeldingTorch")

################ SET INITIAL JOINT ANGLES #################
for j, u in zip(c_arm,u_arm):
    j.set_joint_position(0)
    u.set_joint_position(0)
for j,u,s in zip(c_hand,u_hand,s_hand):
    pr.step()
    j.set_joint_target_velocity(0.04)
    u.set_joint_target_velocity(0.04)
    s.set_joint_target_velocity(0.04)
    pr.step()
for i in range(10):
    pr.step()

############### DELETE ####################3
############### DELETE ####################3

# u_shoulder_2.set_joint_position(math.radians(60))
# u_shoulder_3.set_joint_position(math.radians(-20))
# u_shoulder_1.set_joint_position(math.radians(-120))
# u_elbow.set_joint_position(math.radians(-100))
# u_wrist_2.set_joint_position(math.radians(0))
# u_wrist_16.set_joint_position(math.radians(20))

# for i in range(500):
#     pr.step()

# pr.stop()  # Stop the simulation
# pr.shutdown()  # Close the application
############### DELETE ####################3
############### DELETE ####################3


######################################
####### Colaborator START ############
######################################
ranges = [list(range(2,81,2)), #80
    [], #0
    list(range(0,-91,-2)), #-90
    list(range(0,-71,-2)),#-70,
    list(range(2,-11,-2)),#-10
    [],
]
for j, r in enumerate(ranges):
    if len(r)>1 and r[0] > r[1]:
        c_arm[j].set_joint_target_velocity(-step)
    elif len(r)>1 and r[0] < r[1]:
        c_arm[j].set_joint_target_velocity(-step)
pr.step()
reached_target = [False for i in range(len(ranges))]
max_range_len = max([len(r) for r in ranges])
while True:
    for j, r in enumerate(ranges):
        if len(r) <= 1:
            reached_target[j] = True
            continue
        pos = math.degrees(c_arm[j].get_joint_position())
        if r[0] > r[1]:
            # check if we reached the limit
            if r[-1] > pos:
                continue
            else:
                reached_target[j] = [True]
        elif r[0] < r[1]:
            # check if we reached the limit
            if r[-1] < pos:
                continue
            else:
                reached_target[j] = [True]
    if all(reached_target):
        break
    
exit()

# for i in range(max_range_len):
    # for j, r in enumerate(ranges):
#         # if the range is availiable set it to the corresponding joint
#         if i<len(r):
#             c_arm[j].set_joint_position(math.radians(r[i]))
#             # print("setting arm", j, "at position", r[i])
#             pr.step()


######################################
####### Colaborator READY ############
######################################
ranges = [[], #80
    list(range(0,21,2)), #20
    [], #-90
    list(range(-70,-101,-2)),#-100,
    [],#-10
    [] #0,
]
######################################
####### User START ############
######################################

u_ranges = [list(range(0,61,2)), #60
   list(range(0,-21,-2)), #-20
   list(range(0,-121,-2)), #-120,
   list(range(0,-101,-2)),#-100,
   [],
   list(range(0,21,2)) #20
]

max_range_len = max([len(r) for r in ranges+u_ranges])

for i in range(max_range_len):
    for j, r in enumerate(ranges):
        # if the range is availiable set it to the corresponding joint
        if i<len(r):
            c_arm[j].set_joint_position(math.radians(r[i]))
        if i<len(u_ranges[j]):
            u_arm[j].set_joint_position(math.radians(u_ranges[j][i]))       
        if i<len(r) or i<len(u_ranges[j]):
            pr.step()

######################################
####### Colaborator GRIP ############
######################################
ranges = [list(range(80,61,-2)), #60
    list(range(20,31,2)), #30
    list(range(-90,-59,2)), #-60
    [],#-100,
    [],#-10
    list(range(0,23,2)) #22
]
######################################
####### User Handover ############
######################################
u_ranges = [list(range(60,39,-2)), #40
    list(range(-20,20,2)), #-20
    list(range(-120,-99,2)), #-100,
    list(range(-100,-80,2)),#-80,
    list(range(0,-10,-2)), #-10
    [] #20
]

max_range_len = max([len(r) for r in ranges+u_ranges] )
for i in range(max_range_len):
    for j, r in enumerate(ranges):
        # if the range is availiable set it to the corresponding joint
        if i<len(r):
            c_arm[j].set_joint_position(math.radians(r[i]))
        if i<len(u_ranges[j]):
            u_arm[j].set_joint_position(math.radians(u_ranges[j][i]))       
        if i<len(r) or i<len(u_ranges[j]):
            pr.step()


# CLOSE
c_middle_1.set_joint_target_velocity(-0.04)
c_indexthumb_1.set_joint_target_velocity(-0.04)
c_indexthumb_2.set_joint_target_velocity(-0.02)
for i in range(10):
    pr.step()

# Attatch Tweezers
tweezers.set_parent(c_hand_shape)
pr.step()


######################################
####### Colaborator HANDOVER ############
######################################
ranges = [list(range(60,111,2)), #110
    list(range(30,100,2)), #100
    list(range(-60,-80,-2)), #-80
    list(range(-100,-70,2)),#-70,
    [],#-10
    list(range(22,-1,-2)) #0
] 

max_range_len = max([len(r) for r in ranges])
for i in range(max_range_len):
    for j, r in enumerate(ranges):
        # if the range is availiable set it to the corresponding joint
        if i<len(r):
            c_arm[j].set_joint_position(math.radians(r[i]))
            # print("setting arm", j, "at position", r[i])
            pr.step()

# Attatch Tweezers
tweezers.set_parent(u_hand_shape)
pr.step()

# CLOSE USER HAND
u_middle_1.set_joint_target_velocity(-0.04)
pr.step()
u_middle_2.set_joint_target_velocity(-0.04)
pr.step()
u_indexthumb_1.set_joint_target_velocity(-0.04)
pr.step()
u_indexthumb_2.set_joint_target_velocity(-0.04)
pr.step()

# OPEN COLAB HAND
c_middle_1.set_joint_target_velocity(0.04)
c_indexthumb_1.set_joint_target_velocity(0.04)
c_indexthumb_2.set_joint_target_velocity(0.04)
for i in range(12):
    posx,posy,posz = tweezers.get_position()
    posz += 0.002
    posy += 0.002
    tweezers.set_position([posx,posy,posz]) 
    x,y,z = tweezers.get_orientation()
    y -= math.radians(7) 
    tweezers.set_orientation([x,y,z])
    pr.step()



######################################
####### Colaborator GLASS ############
######################################
ranges = [list(range(110,59,-2)), #60
    list(range(100,49,-2)), #50
    list(range(-80,-59,2)), #-60
    list(range(-70,-40,2)),#-40,
    [],#-10
    list(range(20,7,-2)) #8
] 

######################################
####### User PIECE PICKUP ############
u_ranges = [list(range(40,0,-2)), #0
    list(range(20,75,2)), #74
    list(range(-100,0,2)), #-0,
    list(range(-80,-21,2)),#-20,
    [], #-10
    [] #20
]
max_range_len = max([len(r) for r in ranges+u_ranges] )
for i in range(max_range_len):
    for j, r in enumerate(ranges):
        # if the range is availiable set it to the corresponding joint
        if i<len(r):
            c_arm[j].set_joint_position(math.radians(r[i]))
        if i<len(u_ranges[j]):
            u_arm[j].set_joint_position(math.radians(u_ranges[j][i]))       
        if i<len(r) or i<len(u_ranges[j]):
            pr.step()

### ATTACH PIECE ###
electronic.set_parent(tweezers)
glass.set_parent(c_hand_shape)
pr.step()

#CLOSE Collab hand fully
c_middle_1.set_joint_target_velocity(-0.04)
pr.step()
c_middle_2.set_joint_target_velocity(-0.04)
pr.step()
c_indexthumb_1.set_joint_target_velocity(-0.04)
pr.step()
c_indexthumb_2.set_joint_target_velocity(-0.04)
pr.step()
    



######################################
####### User PIECE Place ############
u_ranges = [list(range(0,71,2)), #70
    list(range(74,65,-2)), #66
    list(range(0,-49,-2)), #-50,
    list(range(-20,-85,-2)),#-84,
    [], #-10
    [] #20
]

max_range_len = max([len(r) for r in u_ranges] )
for i in range(max_range_len):
    for j, r in enumerate(u_ranges):
        # if the range is availiable set it to the corresponding joint
        if i<len(r):
            u_arm[j].set_joint_position(math.radians(r[i]))
        new_j_val = c_arm[j].get_joint_position() + math.radians(2*random.randint(-1,1))
        c_arm[j].set_joint_position(new_j_val)
        pr.step()

            


######################################
####### Soldering READY ############
u_ranges = [list(range(0,-70,-2)), #-70
    list(range(0,40,2)), #40
    list(range(0,70,2)), #70,
    [],#0
    [],#0
    [] #0
]
# for random thing
max_range_len = max([len(r) for r in u_ranges] )
for i in range(max_range_len):
    for j, r in enumerate(u_ranges):
        # if the range is availiable set it to the corresponding joint
        if i<len(r):
            s_arm[j].set_joint_position(math.radians(r[i]))
        new_j_val = c_arm[j].get_joint_position() + math.radians(2*random.randint(-1,1))
        c_arm[j].set_joint_position(new_j_val)
        pr.step()

#c_shoulder_2.set_joint_position(50)
#c_elbow.set_joint_position(-40)
#pr.step()

#time.sleep(3)

######################################
####### Soldering PICKUP ############
u_ranges = [[], #-70
    list(range(40,71,2)), #70
    list(range(70,25,-2)), #26,
    list(range(0,-45,-2)),# -45
    list(range(0,-20,-2)),# -20
    [] #0
]
# for random thing
max_range_len = max([len(r) for r in u_ranges] )
for i in range(max_range_len):
    for j, r in enumerate(u_ranges):
        # if the range is availiable set it to the corresponding joint
        if i<len(r):
            s_arm[j].set_joint_position(math.radians(r[i]))
        new_j_val = c_arm[j].get_joint_position() + math.radians(2*random.randint(-1,1))
        c_arm[j].set_joint_position(new_j_val)
        pr.step()

# Attatch Tweezers
torch.set_parent(s_hand_shape)
pr.step()

# CLOSE Soldering tool fully
s_middle_1.set_joint_target_velocity(-0.04)
pr.step()
s_middle_2.set_joint_target_velocity(-0.04)
pr.step()
s_indexthumb_1.set_joint_target_velocity(-0.04)
pr.step()
s_indexthumb_2.set_joint_target_velocity(-0.04)
pr.step()



######################################
####### Soldering USE ############
u_ranges = [list(range(-70,-50,2)), #-50
    list(range(70,49,-2)), #50
    list(range(25,51,2)), #50,
    list(range(-45,-75,-2)),# -74
    [],# -20
    [] #0
]
# for random thing
max_range_len = max([len(r) for r in u_ranges] )
for i in range(max_range_len):
    for j, r in enumerate(u_ranges):
        # if the range is availiable set it to the corresponding joint
        if i<len(r):
            s_arm[j].set_joint_position(math.radians(r[i]))
        new_j_val = c_arm[j].get_joint_position() + math.radians(2*random.randint(-1,1))
        c_arm[j].set_joint_position(new_j_val)
        pr.step()

pr.stop()  # Stop the simulation
pr.shutdown()  # Close the application
