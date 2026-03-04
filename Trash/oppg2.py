import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as ani
import random as rand

# Konstanter
T=1
Kb=1
beta=1/T/Kb

dt=1
h=1
max_t=100
num_par=101
e=np.e


def V(x):
    return 1

def pp(x,V):
    p = 1/(1+e**(-beta*(V(x-1)-V(x+1)))+e**(-beta*(V(x)-V(x+1))))
    return p

def po(x,V):
    p = 1/(1+e**(-beta*(V(x-1)-V(x)))+e**(-beta*(V(x+1)-V(x))))
    return p

def pm(x,V):
    p = 1/(1+e**(-beta*(V(x+1)-V(x-1)))+e**(-beta*(V(x)-V(x-1))))
    return p

def random_step(x,h,V):
    r= rand.random()
    if (r<pm(x,V)):
        return -h
    elif (r>1-pp(x,V)):
        return h
    else:
        return 0

def simulation(start_pos,max_t,h, V):
    XX=start_pos
    for i in range(0,max_t):
        for j in range(0,np.size(XX)):
            XX[j]=XX[j]+random_step(XX[j],h,V)
    return XX

def multiSim(N,start_pos,max_t,h, V = V):
    totXX=np.array([0])
    for i in range(N):
        XX = simulation(start_pos,max_t,h, V)
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

#animate(simulation())
start_pos=np.arange(-50,51,h)
plt.figure("d")
plt.hist(multiSim(100,start_pos,max_t,h),bins=20,density=True)
plt.show()

