import numpy as np
from numpy import (linspace, logspace, zeros, ones, outer, meshgrid,
                   pi, sin, cos, sqrt, exp)
import matplotlib.pyplot as plt

def findDelta(y_axe, y_axe2):
    n = 100
    m = 3783
    delta = []
    x_axe = []
    counter = 0
    once = True
    fig, ax = plt.subplots()
    for i in range(0, n):
        print ('new')
        delta.append([])
        for j in range(0, m):
            delta[i].append(y_axe[i][j] - y_axe2[i][j])
            counter += 1
            if (once == True):
                x_axe.append(i)
            print(y_axe[i][j] - y_axe2[i][j])
        once = False
        print ('Counter:', counter)
    # for k in range(0, 100):
    #     ax.plot(x_axe, delta[k])
    # plt.show()
    return (delta)
