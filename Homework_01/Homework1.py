from __future__ import division
from numpy import *
from math import *
from pylab import *
import matplotlib.pyplot as plt
import random

#------------------------------------------------
#Random points

x = [random.random() for _ in range (0,10)]
y = [random.random() for _ in range (0,10)]
print(x,y)

plt.plot(x,y, 'o', color='black')
plt.show()


#-------------------------------------------------
#Stern-Gerlach

N = 1e6
i = 0
spin_list = []
diff_list = []
spin=random.randint(0,1)
step = 1000

while i < N:
    spin = random.randint(0,1)
        #random spin number, 0 or 1
    spin_list.append(spin)
        #creates a list with spin values
    spin1 = spin_list.count(1)
        #counts spin values of 1
    spin0 = spin_list.count(0)
    diff = abs(spin1 - spin0)
    diff_list.append(diff)
    i = i + step

x = linspace(0, 1e6, step)
plot(x, diff_list)
xlabel('# particles')
ylabel('spin difference')
show()
