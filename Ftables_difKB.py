
from matplotlib.pyplot import (axes,axis,title,legend,figure,
                               xlabel,ylabel,xticks,yticks,
                               xscale,yscale,text,grid,
                               plot,scatter,errorbar,hist,polar,
                               contour,contourf,colorbar,clabel,
                               imshow)
import matplotlib.pyplot as plt

import os
import glob
from mpl_toolkits.mplot3d import Axes3D
from numpy import (linspace, logspace, zeros, ones, outer, meshgrid,
                   pi, sin, cos, sqrt, exp)
import numpy as np
import instruments as inst

h_apg = []
h_apg.append('h_apg_200_300_h_prg_200_300_kb_s')  # 0
h_apg.append('h_apg_250_h_prg_1000_kb_s')  # 1
h_apg.append('h_apg_300_400_h_prg_300_400_kb_s')  # 2
h_apg.append('h_apg_400_500_h_prg_400_500_kb_s')  # 3
h_apg.append('h_apg_500_600_h_prg_500_600_kb_s')  # 4
h_apg.append('h_apg_600_700_h_prg_600_700_kb_s')  # 5
h_apg.append('h_apg_700_800_h_prg_700_800_kb_s')  # 6

date = []
date.append('2000_11_2')  # 0
date.append('2001_9_2')  # 1
date.append('2014_7_2')  # 2
date.append('2016_3_2')  # 3
date.append('2019_10_2')  # 4

shortDate = []
shortDate.append('2000_11')  # 0
shortDate.append('2001_09')  # 1
shortDate.append('2014_07')  # 2
shortDate.append('2016_03')  # 3
shortDate.append('2019_10')  # 4

nko = []
nko.append('43552')  # 0
nko.append('11745')  # 1
nko.append('41765')  # 2
nko.append('45916')  # 3
nko.append('479')  # 4
nko.append('716')  # 5
nko.append('36936')  # 6

surface2D = 'данные_статья/'
surface3D = 'данные_статья_surface/'

# Форматирование числа до одного знака после запятой
def toFixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"


# Заполнение индексов под константные переменные в массивах выше
def setIndexes(nkoInd, dateInd, h_apgInd):
    return nkoInd, dateInd, h_apgInd


# Изменение дирректории
def changeDir(fileIndex, nkoInd, dateInd, h_apgInd):
    localPath = '/Users/georgijmarinenko/Desktop/ВЫМПЕЛ/Репенские чтения/'
    path = localPath + surface3D + h_apg[h_apgInd] + '/' + nko[nkoInd] + '/'

    path = path + str(fileIndex) + '/dist_nko_' + nko[nkoInd] + '_' + str(fileIndex) + '00000_FTables_orb_' + date[
        dateInd] + '_nko_' + nko[nkoInd] + '_' \
           + str(fileIndex) + '00000_FTables_' + shortDate[dateInd] + '_orb_' + date[dateInd]
    print('nko: ', nko[nkoInd])
    return path


# Чтение данных из файла, формирование двумерного списка
def createLines(typeOFSurface, nkoInd, dateInd, h_apgInd):
    step = 0.1  # Интервальный шаг (КБ)
    counter = 0  # Счетчик кол-ва элементов
    firstLine = True
    x_axe = []
    y_axe = []
    z_axe = []

    for fileCounter in range(0, 100):
        if (typeOFSurface == 2):
            y_axe.append([])
        elif (typeOFSurface == 3):
            y_axe.append([])
            z_axe.append([])
        fileIndex = step
        step += 0.1
        fileIndex = toFixed(fileIndex, 1)
        fPath = changeDir(fileIndex, nkoInd, dateInd, h_apgInd)
        print("fileCounter: ", fileCounter)
        counter = 0
        with open(fPath, 'r') as data:
            for line in data.readlines():
                if (firstLine):
                    firstLine = False
                    continue
                parts = line.split('\t')
                # x_axe.append(float(parts[0]))
                if (typeOFSurface == 2):
                    y_axe[fileCounter].append(float(parts[1]))
                elif (typeOFSurface == 3):
                    y_axe[fileCounter].append(float(parts[1]))
                    z_axe[fileCounter].append(float(parts[2]))
                counter += 1
        firstLine = True
        print('lines: ', counter)
        print(y_axe[fileCounter])
    for i in range(0, counter):  # создание оси Х
        x_axe.append(i)
    print(counter)
    return x_axe, y_axe, z_axe


fig, ax = plt.subplots()
nkoInd, dateInd, h_apgInd = setIndexes(0, 1, 0)
x_axe, y_axe, z_axe = createLines(3, nkoInd, dateInd, h_apgInd)
# x_axe2, y_axe2, z_axe2 = createLines(3, nkoInd, 4, h_apgInd)
# delta = inst.findDelta(y_axe, y_axe2)
# ax.set_xlabel(r'$время, сут. * 1000$')
# ax.set_ylabel(r'$расстояние между двумя точками в (x,y,z)$')
#
# fig.set_figwidth(11)
# fig.set_figheight(7)
# title1 = h_apg[h_apgInd] + '      FTables_orb: ' + date[dateInd] + '      dist_nko: ' + nko[nkoInd]
# plt.title(title1)
# for i in range(0, 100):
#     ax.plot(x_axe, delta[i])
# KB = 0.1
# for i in range(0,100):
#     print ('Max from ', toFixed(KB*i + 0.1, 1), ": ", toFixed(max(delta[i]), 3))
# plt.show()
fig = plt.figure()
print (x_axe, '\n', y_axe[0], "\n", z_axe[0])
ax = plt.axes(projection ='3d')
# ax.plot_surface(np.array(x_axe) , np.array(y_axe[0]), np.array(z_axe[0:1]),rstride=1,cstride=1,cmap='gnuplot')
for i in range(0, 100):
    ax.plot(x_axe , y_axe[i], np.array(z_axe[i]))
print ("delta:")
plt.show()

