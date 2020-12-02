# -*- coding: utf-8 -*-
"""
Ernie Argel
017984237
"""

def main():
    
    def RNG():
        r = []
        # Below are the constants for the rng.
        N = 10000 # The norm.
        A = 4875 # The adder.
        M = 8601 # The multiplier.
        # ------------------------------------------
        # Get seed from clock.
        import time
        S = time.time() - time.process_time()
        # ------------------------------------------
        
        print("You'll be asked to enter a seed.")
        S = int(input('Enter a seed.'))
        
        for i in range(25):
            S = (M*S + A) % N
            v = S/N # Random numbers onthe interval [0, 1)
            #print('%.4f' %r)
            #print(format(r, '.4f'))
            r.append(v)
        
        # -----------------------------------------
        return r
    def die(r):
        import math
        # Die roll
        print("Die Roll")
        for k in range(25):
            die = math.floor(6*r[k] + 1)
            print(die)
    def coin(r):
        import math
    # Coin Flip
        print("Coin Flip")
        for k in range(25):
            coin = math.floor(2*r[k] + 1)
            print(coin)
        
    r = RNG()
    die(r)
    coin(r)
    
main()
    