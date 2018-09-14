from __future__ import division
from numpy import *
from math import *
from pylab import *
import matplotlib.pyplot as plt
import random

#HW02 Random Walk

# constants
d = 1  # distance of a step
N = 20  # total number of steps
steps = [0] * N  # generate a vector


# function of one dimensional random walk
def Walk(n):  # n = number of random walks
    a = 0
    Pos_list = []
    while a <= n:
        Pos = 0  # initial position at x = 0
        for i in range(N):
            x = randint(0, 2)
            if x == 0:
                x = x - 1
            steps[i] = x
            Pos = Pos + d * steps[i]
        Pos_list.append(Pos)
        a = a + 1
    return Pos_list
    

freq = Walk(1000)  # for n random walks

x = linspace(-N, N, 21)
count = [] #counts how many times a distance occurs
for i in range(N + 1):
    c = freq.count(2 * i - 20)
    count.append(c)

print(count)

figure()
plot(x, count)
xlabel('Distance Walked (x)')
ylabel('Frequency of x distance')
title('Probability of a Random 20 Step Walk')
ylim(0,200)



#Finding x^2
n = int(N)
x2 = [0] * n
for i in range(n):
    x2[i] = (2 * i) ** 2


x2_count = []
for i in range(N + 1):
    freq[i] = freq[i] ** 2
for j in range(n):
    c = freq.count((2 * j) ** 2)
    x2_count.append(c)
print(x2)
print(x2_count)


figure()
plot(x2, x2_count)
xlabel('Distance Walked Squared(x^2)')
ylabel('Frequency of x^2')
title('x^2 of Random 20 Steps')
xlim(0,200)




#2 Dimensional Walk
def Walk_2D(n):  # n the number of times the person did random walks
    j = 0
    xpos_list = []
    ypos_list = []
    steps_x = [0] * N  # generate an empty list for x steps
    steps_y = [0] * N  # generate an empty list for y steps
    while j <= n:
        xpos = 0  # initially the person is at x = 0
        ypos = 0  # initially the person is at y = 0
        for i in range(N):
            x = randint(0, 2)
            y = randint(0, 2)
            if x == 0:
                x = x - 1
            if y == 0:
                y = y - 1
            steps_x[i] = x
            steps_y[i] = y
            xpos = xpos + d * steps_x[i]
            ypos = ypos + d * steps_y[i]
        xpos_list.append(xpos)
        ypos_list.append(ypos)
        j = j + 1
    return (xpos_list, ypos_list)

W2 = Walk_2D(1000)
x = W2[0]
y = W2[1]

figure()
plt.scatter(x, y, alpha=0.5)
xlabel('x distance ')
ylabel('y distance')
title('2-D Walk')
show()
        




