import tqdm
import numpy as np
import matplotlib.pyplot as plt

#konstanter

def V_1(
        x : np.ArrayLike,
        k : float       = 1,
        N_x : float     = 100,
        alpha : float   = 0.8
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
    mask = x_modN <= alpha * N_x

    pot = -k*(x_modN-N_x)/((1 - alpha)*N_x)
    pot[mask]  =(k * x_modN/(alpha * N_x))[mask]

    return pot
    
def V_2(*args) -> int:
    return 1

def probabilities(
        V : function,
        x_0 : np.ArrayLike,
        *args
        ) -> np.ArrayLike : 
    """
    params:
        V:    potensialfunksjonen sannsynlighetene beregnes ut ifra
        x_0:      ArrayLike med posisjoner, hvis sannsynlighet for forflyttning skal finnes
        *args:  parameterene som potensialet tar inn

    return:
        
    """

    pot_minus = V(x_0 - 1, *args)
    pot_zero  = V(x_0, *args)
    pot_plus  = V(x_0 + 1, *args)

    p_minus = (1 + np.exp(pot_minus - pot_plus) + np.exp(pot_minus - pot_zero))**-1
    #p_zero = (1 + np.exp(pot_zero - pot_plus) + np.exp(pot_zero - pot_minus))**-1
    p_plus = (1 + np.exp(pot_plus - pot_zero) + np.exp(pot_plus - pot_minus))**-1
    
    return p_minus, p_plus

def simulate3(
        alpha : float, 
        T_p : int, 
        N_x : int, 
        N_p : int, k : int,
        spatialPeriods : int,
        cycles : int):
    
    N = N_x * spatialPeriods
    x_ref : np.ndarray  = np.arange(N_x * spatialPeriods + 1)
    x_0 : np.ndarray = np.asarray([x for x in range(N_p//N) for _ in range(N)])

    V : function = [V_1, V_2][c%2] #Bytter potensial to ganger per cycle
    p_1 = probabilities(V_1, x_ref, k = k, N_x = N_x, )
    for c in tqdm(range(2 * cycles), ascii = True, desc = "running half-cycles"):
        pass



