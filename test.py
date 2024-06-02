import random
import numpy as np
import math
from scipy.special import erfinv
import matplotlib.pyplot as plt
from scipy.stats import norm
import seaborn as sns
import time

def poisson_process2(rate, T):
    t = 0
    S_i = []
    while t < T:
        u = np.random.rand()
        S_i.append(t)
        t -= 1/rate * np.log(u)
    return S_i

def psi(T1, ni, u, c, T2, lambda_):
    t = 0
    i = 0
    times = poisson_process2(lambda_, T2)
    etas = np.random.exponential(ni, len(times))
    while t < T1:
        if i < len(times):
            x = u + c * times[i] - np.sum(etas[:i])
            if x < 0:
                return 1
            else:
                t += times[i]
                i += 1
        else:
            return 0
    return 0

mc = 10**4
u = 5              #kapitał początkowy
c = 2              #stała przyrostu          
lambd = 1          #parametr procesu Poissona
ni = 1
T = 5

proc1 = np.zeros(mc)
proc2 = np.zeros(mc)
proc3 = np.zeros(mc)
for i in range(mc):
    proc1[i] = psi(1000,ni,u,c,T,lambd)
    proc2[i] = psi(2000,ni,u,c,T,lambd)
    proc3[i] = psi(100000,ni,u,c,T,lambd)

print(sum(proc1)/len(proc1))
print(sum(proc2)/len(proc2))
print(sum(proc3)/len(proc3))