# Simulation of a continuous uniform RV on [0,1)
"""
EE 381 spring 2020
Project 4
Ernie Argel
017984237
4/20/2020
"""

import math
import random
import matplotlib.pyplot as plt

n = 10000 # It serves our purposes to be a perfect square

x = []
y = []
Lambda = 0.5 # Parameter in the exponential distribution

for i in range(n):
    r = random.uniform(0,1)
    x.append(r) # List of uniform numbers on [0,1)
    e = (-1 / Lambda) * math.log(1 - r, math.e) # The inverse of the CDF of exponential
    y.append(e) # Exponentially distributed random numbers
    
b = max(x)
a = min(x)
R = b - a # Range in the sense of data

intervals = int(math.ceil(math.sqrt(n)))

width = (R / intervals) # Class width

plt.subplot(2, 1, 1)
plt.hist(x, intervals, density = width)
plt.subplot(2, 1, 2)
plt.hist(y, intervals, density = width)




