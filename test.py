import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

def iloraz(n, mi, sigma):
    ys = np.zeros(n)
    i = 0
    while i < n:
        u1, u2 = np.random.rand(2)
        u, e = u1, np.exp(1)
        v = -np.sqrt(2/e) + 2*np.sqrt(2/e) * u2
        x = v / u
        if x**2 <= 2 * (3 - u * (4 - u)):
            ys[i] = sigma * x + mi
            i += 1
        elif (x**2 <= 2/u - 2*u) and (x**2 >= -4 * np.log(u)):
            ys[i] = sigma * x + mi
            i += 1
    return ys

# Generowanie próbek
n = 100000
mi = 0
sigma = 1
samples = iloraz(n, mi, sigma)

# Histogram i wykres gęstości
plt.hist(samples, bins=50, density=True, alpha=0.6, color='g')

# Teoretyczna krzywa rozkładu normalnego
xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
p = stats.norm.pdf(x, mi, sigma)
plt.plot(x, p, 'k', linewidth=2)
title = "Histogram and Normal Distribution Curve"
plt.title(title)
plt.show()