#imports
import numpy as np
import matplotlib.pyplot as plt
from utils import pm, po, pp
import random as rand
from time import perf_counter

#constants
k = 1
N_x = 100
alpha = 0.8
T_p = 50
N_p = 12 * N_x
#functions
def V_1(x : int) -> float:
    x_=x%N_x

    if  (x_<alpha*x):
        return k*x/(alpha*N_x)
    else:
        return -k*(x-N_x)/((1 - alpha)*N_x)
    
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
    current = np.zeros(10)
    x_new=np.zeros_like(x)
    c_i = 0
    #numnext=x[0]
    #num=0
    time=0
    for c in range(10):     
        for t in range(2*T_p):
            for idx in range(len(x)):
                #num=numnext
                #numnext=x[(idx+1)%len(x)]
                for i in range(x[idx]):
                    temp = random_step(x_ref[idx], V_tot(t))
                    n += temp
                    x_new[(idx + temp)%len(x)] += 1
                    #x[idx]-=1

            time=perf_counter()  
            x=x_new
            x_new=x_new*0
            print(c,time-perf_counter())
             
        current[c_i]=n/(N_x * 2*T_p)
        c_i+=1
        n = 0
    return x, current

#andre ting
x_ref = np.arange(-N_x, N_x, 1)
x = np.full(2*N_x, 6)

x_end, current = simulate3a(x,x_ref)
print(x_end, current)