#imports
import numpy as np
import matplotlib.pyplot as plt
from oppg2 import pm, po, pp
import random as rand

#constants
k = 1
N_x = 100
alpha = 0.8
T_p = 500
N_p = 12 * N_x
#functions
def V_1(x : int) -> float:
    lowerBound = -(1-alpha)*N_x
    upperBound = alpha*N_x

    while x < lowerBound: x+= N_x
    while x > upperBound: x-= N_x

    if  alpha*N:
        return k*x/(alpha*N_x)
    else:
        return -k*x/((1 - alpha)*N_x)
    
def V_2(x : int) -> float:
    return 1

def V_tot(t : int) -> float:
    if (t // T_p) % 2:
        return V_1
    else:
        return V_2

def random_step(x, V):
    r= rand.random()

    if (r<pm(x, V)):
        return -1
    elif (r>1-pp(x, V)):
        return 1
    else:
        return 0

def simulate3a(x, x_ref):
    n = 0
    new_x  = np.zeros_like(x)
    current = np.zeros(10)
    c_i = 0
    for t in range(20* T_p):
        for idx in range(len(x)):
            for i in range(x[idx]):
                temp = random_step(x_ref[idx], V_tot(t))
                n += temp
                new_x[(idx + temp)%len(x)] += 1
        x = new_x

        if not t % 2*T_p:
            current[c_i] = n/(N_x * 2*T_p)
            c_i += 1
            n = 0

    return x, current

#andre ting
x_ref = np.arange(-N_x, N_x, 1)
x = np.full(2*N_x, 6)