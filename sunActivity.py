import matplotlib.pyplot as plt
import numpy as np

token = open('EarthAtm.txt','r')
linestoken=token.readlines()
tokens_column_number = 2
counter = 1
resulttoken=[]
for x in linestoken:
    resulttoken.append(x.split()[tokens_column_number])
    counter += 1
x = range(1, counter)
token.close()
print(resulttoken)
print(x)

# fig, ax = plt.subplots()
# ax.plot(x, resulttoken)
n, bin, patches = plt.hist(resulttoken, bins=27000)
plt.show()
