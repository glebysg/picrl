import numpy as np
import math
from scipy import interpolate

def interpol(array_3d,use_full_cos=[False,False,True],no_steps = 40):
    newarray = []
    for index, cos_condition in enumerate(use_full_cos):
        old_range = (array_3d[index][1]-array_3d[index][0])
        step_range = np.arange(0,1+1.0/no_steps,1.0/no_steps)
        if cos_condition:
            cos_range = interpolate.interp1d([0,1], [-180,90])
        else:
            cos_range = interpolate.interp1d([0,1], [0,90])
        array_1d = [math.sin(math.radians(x))*old_range + array_3d[index][0] \
                for x in cos_range(step_range)]
        newarray.append(array_1d)
    print(newarray)
    return (newarray)

if __name__ == "__main__":
    import matplotlib.pyplot as plt
    plt.style.use('seaborn-whitegrid')
    x,y,z = interpol([[10,30],[20,-40],[10,0]],[True, True, False])
    plt.plot(x, z, '-ok');
    plt.plot(y, z, '-xk');
    plt.show()
