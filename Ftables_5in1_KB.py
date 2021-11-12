import matplotlib.pyplot as plt
from matplotlib.pyplot import (axes,axis,title,legend,figure,
                               xlabel,ylabel,xticks,yticks,
                               xscale,yscale,text,grid,
                               plot,scatter,errorbar,hist,polar,
                               contour,contourf,colorbar,clabel,
                               imshow)
from mpl_toolkits.mplot3d import Axes3D
from numpy import (linspace,logspace,zeros,ones,outer,meshgrid,
                   pi,sin,cos,sqrt,exp)
import numpy as np
from itertools import islice

file1 = 'dist_nko_43552_0.100000_FTables_orb_2000_11_2_nko_43552_0.100000_FTables_2000_11_orb_2000_11_2'
file2 = 'dist_nko_43552_0.100000_FTables_orb_2001_9_2_nko_43552_0.100000_FTables_2001_09_orb_2001_9_2'
file3 = 'dist_nko_43552_0.100000_FTables_orb_2014_7_2_nko_43552_0.100000_FTables_2014_07_orb_2014_7_2'
file4 = 'dist_nko_43552_0.100000_FTables_orb_2016_3_2_nko_43552_0.100000_FTables_2016_03_orb_2016_3_2'
file5 = 'dist_nko_43552_0.100000_FTables_orb_2019_10_2_nko_43552_0.100000_FTables_2019_10_orb_2019_10_2'

# Чтение данных из файла, опредедение количества элементов
def createLines(file):
    x_axe = []
    y_axe = []
    counter = 0
    with open(file, 'r') as data:
        for line in data.readlines():
            parts = line.split('\t')
            # x_axe.append(float(parts[0]))
            y_axe.append(float(parts[1]))
            counter += 1
    for time in range(0, counter):
        x_axe.append(time)
    return x_axe, y_axe

x_axe1, y_axe1 = createLines(file1)
x_axe2, y_axe2 = createLines(file2)
x_axe3, y_axe3 = createLines(file3)
x_axe4, y_axe4 = createLines(file4)
x_axe5, y_axe5 = createLines(file5)


xlabel(r'$x$')
ylabel(r'$y$')
# title(r'$\sin x$, $\cos x$',fontsize=20)
plt.subplot (2, 3, 1)
plt.plot(x_axe1, y_axe1, linestyle='', markersize=0.1, color='b', dashes=[5, 0])
plt.title('2000_11_2')

plt.subplot (2, 3, 2)
plt.plot(x_axe2, y_axe2, linestyle='', markersize=0.1, color='r', dashes=[5, 0], label=r'$2001_9_2$')
plt.title('2001_9_2')

plt.subplot (2, 3, 3)
plt.plot(x_axe3, y_axe3, linestyle='', markersize=0.1, color='g', dashes=[5, 0])
plt.title('2014_7_2')

plt.subplot (2, 3, 4)
plt.plot(x_axe4, y_axe4, linestyle='', markersize=0.1, color='y', dashes=[5, 0])
plt.title('2016_3_2')

plt.subplot (2, 3, 5)
plt.plot(x_axe5, y_axe5, linestyle='', markersize=0.1, color='k', dashes=[5, 0])
plt.title('2019_10_2')
# legend(fontsize=20)
plt.show()