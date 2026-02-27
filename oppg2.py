import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as ani
import random as rand
from collections import Counter

# Konstanter
T=1
Kb=1
beta=1/T/Kb

dt=1
h=1
start_distance=1
max_t=200
num_par=101
e=np.e


def V(x):
    return x**2/100

def pp(x):
    p = 1/(1+e**(-beta*(V(x-1)-V(x+1)))+e**(-beta*(V(x)-V(x+1))))
    return p

def po(x):
    p = 1/(1+e**(-beta*(V(x-1)-V(x)))+e**(-beta*(V(x+1)-V(x))))
    return p

def pm(x):
    p = 1/(1+e**(-beta*(V(x+1)-V(x-1)))+e**(-beta*(V(x)-V(x-1))))
    return p

def random_step(x):
    r= rand.random()
    if (r<pm(x)):
        return -h
    elif (r>1-pp(x)):
        return h
    else:
        return 0

def simulation():
    Xo=np.arange(-num_par/2,num_par/2+1,start_distance)
    XX=np.stack([Xo for _ in range(0,round(max_t/dt))])

    for i in range(0,max_t):
        for j in range(0,num_par+1):
            XX[i::,j]=XX[i,j]+random_step(XX[i,j])
    return XX

def multiSim(N):
    totXX=np.array([0])
    for i in range(N):
        XX = simulation()[-1]
        totXX=np.concatenate((totXX,XX))
    return totXX

def animate(XX):
    fig,ax = plt.subplots()
    antall= np.size(XX[0])
    ax.set_xlim(-antall/2,antall/2)
    X=np.arange(0,antall,1)
    
    def update(i):
        plt.cla()
        ax.set_xlim(-antall/2,antall/2)
        ax.plot(XX[i],X,"o")

    animation=ani.FuncAnimation(fig,update,interval=100)
    plt.show()

animate(simulation())

plt.figure("d")
plt.hist(multiSim(100),bins=20,density=True)
plt.show()

