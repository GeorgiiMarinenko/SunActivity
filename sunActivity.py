import matplotlib.pyplot as plt
import numpy as np
from itertools import islice

# Чтение данных из файла, опредедение количества элементов
def fileParser(fileName):
    line = fileName.readlines()
    tokens_column_number = 2
    counter = 1
    y_axe = []
    for x in line:
        y_axe.append(x.split()[tokens_column_number])
        counter += 1
    fileName.close()
    return y_axe, counter


def isint(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def averagePerMonth(y_axe):
    a = np.array(y_axe[:27510])
    nSlices = 30
    a.reshape((nSlices, -1))

    month = 0
    avMonth = []
    for i in range(len(a)):
        month += float(a[i])
        if (i % 30 == 0) and (i != 0):
            avMonth.append(month / 30)
            month = 0
        if i == 27509:
            break
    return (avMonth)

fileName = open('EarthAtm.txt', 'r')
y_axe, counter = fileParser(fileName)
x_axe = range(1, counter)

# print(y_axe)
# print(x_axe)

y = averagePerMonth(y_axe)

fig, ax = plt.subplots()
# horizontal_lines = [1000, 200, 400]
# ax.hlines(horizontal_lines, 0, 20000, color="r")
# ax.set_yticks(np.append(ax.get_yticks(), horizontal_lines))
# ax.text(20000, 0, 10000, ha="left", va="center", color="r")
# ax.plot(x_axe, y_axe)
x = []
for i in range(0, 916):
    x.append(i)
# the main axes is subplot(111) by default
plt.plot(x, y, "r-")
#Ось
plt.axis([0, 917, 0, 400])
plt.xlabel('month')
plt.ylabel('sun activity index')
plt.title('index of sun activity for 76 years')

y_min = np.linspace(0, 12, 1)
y_max = np.linspace(400, 916, 1)
interval = np.arange(24, 936, 12)
print(interval)
ax.vlines(interval, y_min, y_max)
# n, bin, patches = plt.hist(resulttoken, bins = 27000)
plt.show()
