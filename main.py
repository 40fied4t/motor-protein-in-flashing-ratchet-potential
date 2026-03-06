from Scripts import oppg3
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as ani
from Scripts import animationUtils

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


