from Scripts import oppg3
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as ani



def animate(
        XX,
        alpha : float  = 0.8, 
        T_p : int = 500, 
        N_x : int = 100, 
        N_p : int = 1200,
        k : int  = 1,
        spatialPeriods : int  = 2,
        cycles : int = 10
):
    fig,ax = plt.subplots()
    X=np.arange(0,len(XX[0]),1)
    x_ref=np.arange(0,spatialPeriods*N_x,1)
    V=[oppg3.V_1,oppg3.V_2]
    def update(i):
        i=i*20
        Vnow=V[(i//500)%2]
        plt.cla()
        ax.set_xlim((0,spatialPeriods*N_x))
        ax.plot(x_ref,Vnow(x_ref)*N_p)
        ax.plot(XX[i],X,"o")

    animation=ani.FuncAnimation(fig,update,interval=20,frames=T_p*cycles*2/20)
    plt.show()