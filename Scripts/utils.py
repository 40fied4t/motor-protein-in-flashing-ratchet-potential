import numpy as np


e=np.e
beta = 1


def pp(x,V):
    p = 1/(1+e**(-beta*(V(x-1)-V(x+1)))+e**(-beta*(V(x)-V(x+1))))
    return p

def po(x,V):
    p = 1/(1+e**(-beta*(V(x-1)-V(x)))+e**(-beta*(V(x+1)-V(x))))
    return p

def pm(x,V):
    p = 1/(1+e**(-beta*(V(x+1)-V(x-1)))+e**(-beta*(V(x)-V(x-1))))
    return p
