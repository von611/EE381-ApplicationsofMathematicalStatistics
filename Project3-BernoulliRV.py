# -*- coding: utf-8 -*-
"""
EE 381 spring 2020
Project 3
Ernie Argel
017984237
2/24/2020
End Date
Simulating a Bernoulli RV and using it
to make a simple Markov chain

"""


import random

p = float(input('Enter the probability of success. '))
T = int(input('How many trials are wanted. '))

for j in range(T):
    r = random.uniform(0, 1)
    if r < p:
        print('1', end=' ') # Success
    else:
        print('0', end= ' ') # Failure


import random # Importing Pythons RNG

Location = [] # Where the particle is located.

p_A = float(input('Enter the probability of leaving node zero. '))

p_B = float(input('Enter the probability of leaving node one. '))

S = int(input("Enter either a '0' or a '1' to start. ")) # Temporary starting place.
Location.append(S)

for i in range(25):
    r = random.uniform(0, 1) # Generating a uniform random number
    
    if r < p_A and S == 0: # At zero and success 
        S = 1 # Reassign to one
    elif r < p_B and S == 1: # At one and success
        S = 0 # Reassign to zero
    Location.append(S)
    
for i in Location:
    print(i, end= ' ')
    
    
    
    