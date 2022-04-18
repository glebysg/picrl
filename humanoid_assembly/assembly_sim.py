import numpy as np
from pyrep import PyRep
from pyrep.objects.dummy import Dummy

pr = PyRep()
# Launch the application with a scene file in headless mode
pr.launch('../models/assembly.ttt')
pr.start()  # Start the simulation

##### init ###############
c_l_target = Dummy('left_target_c')
c_r_target = Dummy('right_target_c')
u_l_target = Dummy('left_target_u')
u_r_target = Dummy('right_target_u')
c_l_init = Dummy('wlc_0')
c_r_init = Dummy('wrc_0')
##### init ###############

#### Action ###############
c_l_target.set_pose(c_l_init.get_pose())
c_r_target.set_pose(c_r_init.get_pose())
pr.step()
#### Action ###############

# Do some stuff
print('Done ...')
input('Press enter to finish ...')
pr.stop()  # Stop the simulation
pr.shutdown()  # Close the application
