from mpl_toolkits.mplot3d import Axes3D
from numpy import (linspace, logspace, zeros, ones, outer, meshgrid,
                   pi, sin, cos, sqrt, exp)
import numpy as np

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


# Форматирование числа до одного знака после запятой
def toFixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"


# Заполнение индексов под константные переменные в массивах выше
def setIndexes(nkoInd, dateInd, h_apgInd):
    return nkoInd, dateInd, h_apgInd


# Изменение дирректории
def changeDir(fileIndex, nkoInd, dateInd, h_apgInd):
    # nkoInd, dateInd, h_apgInd = nko, date, h_apg
    localPath = '/Users/georgijmarinenko/Desktop/ВЫМПЕЛ/Репенские чтения/'
    path = localPath + 'данные_статья_surface/' + h_apg[h_apgInd] + '/' + nko[nkoInd] + '/'

    path = path + str(fileIndex) + '/dist_nko_' + nko[nkoInd] + '_' + str(fileIndex) + '00000_FTables_orb_' + date[
        dateInd] + '_nko_' + nko[nkoInd] + '_' \
           + str(fileIndex) + '00000_FTables_' + shortDate[dateInd] + '_orb_' + date[dateInd]
    print('nko: ', nko[nkoInd])
    return path


def insertColumn():
    step = 0.1  # Интервальный шаг (КБ)
    counter = 0  # Счетчик кол-ва элементов
    firstLine = True
    nkoInd = 0
    h_apgInd = 0
    while (nkoInd < 6):
        dateInd = 0
        while (dateInd < 5):
            for fileCounter in range(0, 100):
                fileIndex = step
                step += 0.1
                fileIndex = toFixed(fileIndex, 1)
                print (nkoInd, " ", dateInd, " ", h_apgInd)
                fPath = changeDir(fileIndex, nkoInd, dateInd, h_apgInd)
                print("fileCounter: ", fileCounter)
                counter = 0
                with open(fPath, 'r+') as file:
                    lines = file.readlines()
                    file.seek(0, 0)
                    for line in lines:
                        if (firstLine):
                            firstLine = False
                            continue
                        columns = line.strip().split("\t")
                        file.write("\t".join(columns) + "\t" + str(fileIndex) + "\n")
                        print(line)
                        counter += 1
                firstLine = True
            step = 0.1
            dateInd += 1
        nkoInd += 1
        h_apgInd += 1


insertColumn()