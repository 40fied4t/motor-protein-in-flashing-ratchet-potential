import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as ani
import random as rand

T=1
Kb=1
beta=1/T/Kb
e=np.e


def pp(x,V):
    p = 1/(1+e**(-beta*(V(x-1)-V(x+1)))+e**(-beta*(V(x)-V(x+1))))
    return p

def po(x,V):
    p = 1/(1+e**(-beta*(V(x-1)-V(x)))+e**(-beta*(V(x+1)-V(x))))
    return p

def pm(x,V):
    p = 1/(1+e**(-beta*(V(x+1)-V(x-1)))+e**(-beta*(V(x)-V(x-1))))
    return p

def random_step(x,V):
    r= rand.random()
    if (r<pm(x,V)):
        return -1
    elif (r>1-pp(x,V)):
        return 1
    else:
        return 0