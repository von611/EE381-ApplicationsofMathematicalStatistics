# -*- coding: utf-8 -*-
"""
EE 381 Spring 2020
Project 6
Ernie Argel
017984237
Start Date: 5/4/2020
Due Date: 5/6/2020
Markov Random Walk

"""

p= float(input("Enter the probability of a jump."))
S= int(input("Enter the starting position."))
N=int(input("Enter the boundary position."))
J=int(input("Enter the number of jumps wanted."))

import random

for i in range(J):
    r = random.uniform(0,1)
    if S == 0:
        S=1
    if S == N:
        S = N-1
    if(S<N)and(S>0):
        if r < p:
            S=S+1
        else:
            S=S-1
    print(S)