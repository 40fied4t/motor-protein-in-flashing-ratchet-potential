from tqdm import trange
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

    pot = -k*(x_modN-N_x)/((1 - alpha)*N_x)
    pot[x_modN <= alpha * N_x]  =(k * x_modN/(alpha * N_x))[x_modN <= alpha * N_x]

    return pot
    
def V_2(x, *args) -> int:
    return np.zeros_like(x)

def probabilities(
        V : function,
        x_0 : np.ArrayLike,
        k : float,
        N_x : float,
        alpha : float
        ) -> tuple[np.ndarray, np.ndarray] : 
    """
    params:
        V:    potensialfunksjonen sannsynlighetene beregnes ut ifra
        x_0:      ArrayLike med posisjoner, hvis sannsynlighet for forflyttning skal finnes
        *args:  parameterene som potensialet tar inn
    returns:
        
    """

    pot_minus = V(x_0 - 1, k, N_x, alpha)
    pot_zero  = V(x_0, k, N_x, alpha)
    pot_plus  = V(x_0 + 1, k, N_x, alpha)

    p_minus = (1 + np.exp(pot_minus - pot_plus) + np.exp(pot_minus - pot_zero))**-1
    #p_zero = (1 + np.exp(pot_zero - pot_plus) + np.exp(pot_zero - pot_minus))**-1
    p_plus = (1 + np.exp(pot_plus - pot_zero) + np.exp(pot_plus - pot_minus))**-1
    
    return p_minus, p_plus

def simulate3(
        startPositions : np.ndarray = None,
        alpha : float  = 0.8, 
        T_p : int = 500, 
        N_x : int = 100, 
        N_p : int = 1200,
        k : int  = 1000,
        spatialPeriods : int  = 2,
        cycles : int = 10,
        startV_2 : bool = False
        )-> tuple[np.ndarray, np.ndarray, list]:
    """
    params:
        startPositions: array over startposisjoner, hvis None brukes fylles alle posisjoner
        alpha: konstant, forskyver potensialet
        T_p: tidsperiode for en halv syklus
        N_x: romlig periode for potensial
        N_p antall partikler, rundes av til multiplum av antall len(startPositions)
        k: samlet konstant lik k * beta
        spatialPeriods: antall romlige perioder, gir antall festepunkter som N_p * spatialPeriods
        cycles: antall sykler som skal simuleres
        startV_2: hvis True starter blir V_2 det første potensialet
    returns:
        x: array med sluttposisjoner
        currents: array
        XX: matrise med posisjoner for hvert tidssteg slik at x(t) = X[t]
    """

    
    N = N_x * spatialPeriods #antall festepunkter
    XX = [] 
    x_ref : np.ndarray  = np.arange(N) #referansearray for x-aksen. Verdier samsvarer med indeks for referansearrayer
    
    if startPositions == None:
        startPositions = x_ref

    x_0 : np.ndarray = np.asarray([i for i in startPositions for _ in range(N_p//len(startPositions))]) #array med alle partikler
    XX.append(x_0)

    p_1 = probabilities(V_1, x_ref, k, N_x, alpha)
    p_2 = probabilities(V_2, x_ref, k, N_x , alpha)

    pm_tup = (p_1[0], p_2[0])
    pp_tup = (p_1[1], p_2[1])

    n = np.zeros_like(x_0)

    currents = np.zeros(cycles)
    for c in trange(2 * cycles, ascii = True, desc  = "runnning half-cycles"):
        pm_ref  = pm_tup[c%2 - int(startV_2)]
        pp_ref =  pp_tup[c%2 - int(startV_2)]

        for t in range(T_p):
            x = x_0%N
            pm = np.asarray([pm_ref[i] for i in x])
            pp = np.asarray([pp_ref[i] for i in x])

            r = np.random.rand(N_p)
            x[r < pm] -= 1
            x[1 - pp < r] += 1

            n += x - x_0%N
            x_0 = x

            XX.append(x_0)
            
        if c%2:
            currents[c//2] = np.mean(n)/(2 * T_p)
            n = np.zeros_like(x)

    return x, currents, XX
