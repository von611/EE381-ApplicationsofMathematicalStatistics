# -*- coding: utf-8 -*-
"""
EE 381 spring 2020
Project 2
Ernie Argel
017984237
2/10/2020
"""
import math

Coin = [] # List of coin flips

N = 10000 # The norm.
A = 4987 # The adder.
M = 122021 # The multiplier.
# ------------------------------------------
# ------------------------------------------
S = float(input("Enter a seed value. "))

for i in range(100000):
    S = (M*S + A) % N
    v = S/N # Random numbers onthe interval [0, 1)
    coin = math.floor(2*v)
    Coin.append(coin)
# Above generate list of coin flips
#-----------------------------------
    
game = [] # One trial of game
count = 0 # Accumulator for number of flips
win = 0 # Accumulator for number of wins

for i in Coin:
    game.append(i)
    if i == 1: #We have flipped a head
        count = count + 1
        L = len(game) # How many flips before head
        if L % 2 == 1: # We have a head on an odd flip
            win = win + 1 # Increment the 'win' record
        game = [] # Refresh for a new game
p = win / count
print(p)