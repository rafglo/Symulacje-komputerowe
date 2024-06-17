import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import scipy.stats as sp

def poisson_process(lambd, T, num_samples):
    N_t = np.zeros(num_samples)
    for k in range(num_samples):
        bell = np.random.exponential(1/lambd)
        t = 0
        i = 0
        while t < T:
            i += 1
            t += bell
            bell = np.random.exponential(1/lambd)
        N = i - 1
        N_t[k] = N
    return N_t

lambd = 2
T = 10
num_samples = 10**4

data = poisson_process(lambd, T, num_samples)
L = len(np.unique(data))

T2 = range(0,40)
pois = sp.poisson.pmf(T2, lambd*T)

sns.histplot(data, stat='probability')
plt.scatter(T2, pois)
plt.plot(T2, pois, "b--")

plt.legend()
plt.show()