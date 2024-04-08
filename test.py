import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm 

import numpy as np

def cauchy_sample(n):
    # Generowanie par X, Y z rozkładu jednostajnego
    X = np.random.uniform(size=n)
    Y = np.random.uniform(size=n)

    # Wyliczenie wartości gęstości f(x) = ch(x)
    f = np.cosh

    # Zwrócenie Z = Y/X
    return Y / X

def normal_sample(n):
    # Generowanie par X, Y z rozkładu jednostajnego
    X = np.random.uniform(size=n)
    Y = np.random.uniform(size=n)

    # Wyliczenie wartości gęstości f(x) = ch(x)
    f = np.cosh

    # Zwrócenie Z = Y/X
    return Y / X

# Przykład użycia
cauchy_samples = cauchy_sample(1000)
normal_samples = normal_sample(1000)
# Wykres próbek
xs = np.linspace(-5,5, 100)
plt.hist(normal_samples, bins=50, density=True, alpha=0.5, color='b', label='Samples')
plt.plot(xs, norm.pdf(xs, 0, 1), label="gęstość teoretyczna")
plt.title('Histogram and Density')
plt.xlabel('Value')
plt.ylabel('Density')
plt.legend()
plt.show()
# Wyświetlenie wyników
