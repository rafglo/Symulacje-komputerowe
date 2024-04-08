import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm 

def ziggurat(f, g, k, x_0, x_k, n, c):
    xs = np.linspace(x_0, x_k, k)
    samples = []
    f_min = []
    f_max = []
    for i in range(k-1):  # Zmieniono z range(k)
        f_min.append(min([f(j) for j in np.linspace(xs[i], xs[i+1], 10**3)]))
        f_max.append(max([f(j) for j in np.linspace(xs[i], xs[i+1], 10**3)]))
    while len(samples) < n:
        u = np.random.uniform()
        x = np.random.uniform(x_0, x_k - (x_k - x_0) * 1e-10)
        ind = 0
        for i in range(k-1):  # Zmieniono z range(k)
            if i == k - 2 and xs[i] <= x <= x_k:  # Zmieniono z k - 1
                ind = i
                break
            elif xs[i] <= x < xs[i+1]:
                ind = i
                break
        if u * c * g(x) < f_min[ind]:
            samples.append(x)
        elif u * c * g(x) > f_max[ind]:
            continue
        else:
            if u * c * g(x) < f(x):
                samples.append(x)
    return samples

def exp_cdf(x):
    return np.exp(-x)

# Definicja funkcji gęstości docelowej
def target_density(x):
    return np.exp(-x**2 / 2) / np.sqrt(2 * np.pi)

# Wywołanie funkcji ziggurat
samples = ziggurat(target_density, lambda x: 1 / np.sqrt(2 * np.pi), 100, -4, 4, 10000, 1)

# Obliczenie wartości gęstości dla wygenerowanych próbek
density_values = [target_density(x) for x in samples]

# Wykres próbek
plt.figure(figsize=(8, 6))
plt.hist(samples, bins=50, density=True, alpha=0.5, color='b', label='Samples')
plt.plot(samples, density_values, 'r.', label='Density')
plt.title('Histogram and Density')
plt.xlabel('Value')
plt.ylabel('Density')
plt.legend()
plt.show()
# Wyświetlenie wyników
