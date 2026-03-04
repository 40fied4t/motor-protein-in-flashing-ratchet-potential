#Imports
import numpy as np
import matplotlib.pyplot as plt
from utils import pm,po,pp
import matplotlib.animation as ani


N_x=20
T_p=40
alpha=0.2
beta=1000
k=1
h=1 #stepsize
b=2


def random_step(x,V):
    length=len(x)
    #Lager et array med tilfeldige tall for å avgjøre hvilken retning
    r=np.random.rand(length)

    #Lager et array med indexer for x i en tilfeldig rekkefølge
    idx=np.arange(0,length,1)
    np.random.shuffle(idx)
    
    for i in idx:
        if (r[i]<pm(x[i],V) and abs(x[i]-x[i-1])%(N_x*4)>=(b+h)): # Sjekker steg retning og bevegelse ikke gir krasj
            x[i]-=h
        elif (r[i]>(1-pp(x[i],V)) and abs(x[i]-x[i-length+1])%(N_x*4)>=(b+h)):
            x[i]+=h
    return x

def V_1_array(
        x : np.ArrayLike
        ) -> np.ArrayLike : 
    """
    params:
        x:      Arraylike med heltallsposisjoner
        k:      konstant som tilsvarer k * beta
        N_x:    antall binding sites i én periode
        alpha:  konstant
    return:
        pot:    Potentialet V_1
    """
    x_modN =x%N_x
    #mask = x_modN <= alpha * N_x

    pot = -k*(x_modN-N_x)/((1 - alpha)*N_x)
    pot[x_modN <= (alpha * N_x)]  =(k * x_modN/(alpha * N_x))[x_modN <= (alpha * N_x)]

    return pot

def V_1(x : int) -> float:
    x_=x%N_x

    if  (x_<alpha*x):
        return k*x/(alpha*N_x)
    else:
        return -k*(x-N_x)/((1 - alpha)*N_x)
    
def V_2(x : int) -> float:
    return np.full_like(x,k)

def V_tot(t : int) -> float:
    if (t // T_p) % 2:
        return V_1
    else:
        return V_2
    

def simulate(x,cycles):
    n=0
    XX=np.zeros((cycles*T_p*2+1,len(x)))
    XX[0]=x
    currents=np.zeros(cycles)
    for c in range(cycles):
        for t in range(T_p*2):
            XX[c*T_p*2+t+1]=random_step(XX[c*T_p*2+t],V_tot(t))
            n+=np.sum(XX[c*T_p*2+t+1]-XX[c*T_p*2+t])
        currents[c]=n/(T_p*2/N_x)
    return XX%(4*N_x),currents

def animate(XX):
    fig,ax = plt.subplots()
    ax.set_xlim(0,N_x*4)
    Y=np.zeros(len(XX[0]))
    #Y=np.arange(0,20,1)
    x_v=np.arange(0,N_x*4+1,1)
    def update(i):
        V=[V_2,V_1_array][(i//T_p)%2]
        plt.cla()
        ax.set_xlim(0,N_x*4)
        ax.plot(x_v,V(x_v))
        ax.scatter(XX[i],Y,c=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f','#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f'])

    animation=ani.FuncAnimation(fig,update,interval=100,frames=len(XX))
    plt.show()

x_start=np.arange(0,N_x*4,5)
cycles=5
XX ,currents= simulate(x_start,cycles)
print(currents)

plt.figure(figsize=(15,8))
for i in range(len(XX[0])):
    plt.plot(XX[:,i],".")
plt.show()


animate(XX)