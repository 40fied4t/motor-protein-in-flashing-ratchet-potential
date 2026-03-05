from Scripts import oppg3
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as ani

def animate(XX):
    fig,ax = plt.subplots()
    X=np.arange(0,len(XX[0]),1)
    x_ref=np.arange(0,200,1)
    V=[oppg3.V_1,oppg3.V_2]
    def update(i):
        i=i*20
        Vnow=V[(i//500)%2]
        plt.cla()
        ax.set_xlim((0,200))
        ax.plot(x_ref,Vnow(x_ref)*1200)
        ax.plot(XX[i],X,"o")

    animation=ani.FuncAnimation(fig,update,interval=20)
    plt.show()


def main():

    """
    x = np.arange(200)
    plt.plot(x, oppg3.V_1(x))
    plt.show()
    """
    # x, currents, XX = oppg3.simulate3(k=1000)


    # print(x)
    # print(currents)
    # print(sum(currents))
    # animate(XX)

    T_p_list = [i for i in range(1, 1001, 20)]
    startPositions = np.array([0, 100])
    n = len(T_p_list)
    print(n)
    curr_avg = np.zeros(n)
    for i in range(n):
        x, currents, XX = oppg3.simulate3(
            T_p = T_p_list[i],
            cycles = 1,
            alpha = 0.8,
            N_p = 4000,
            startPositions = startPositions,
            startV_2=True)
        
        curr_avg[i] = np.mean(currents)

    plt.plot(T_p_list, curr_avg)
    plt.title("$J_{avg}$ som funksjon av $T_p$")
    plt.xlabel("$T_p$")
    plt.ylabel("$J_{avg}$")
    plt.grid()
    plt.savefig("Output/J_avg.png")

if __name__ == "__main__":
    main()


