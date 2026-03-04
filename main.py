from Scripts import oppg3
import numpy as np
import matplotlib.pyplot as plt

def main():

    # x = np.arange(200)
    # plt.plot(x, oppg3.V_1(x))
    # plt.show()

    x, currents, XX = oppg3.simulate3(alpha = 0.8, k = 10)

    print(x)
    print(currents)
    print(sum(currents))


if __name__ == "__main__":
    main()
