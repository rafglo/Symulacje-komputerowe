import numpy as np
from scipy.stats import poisson
import matplotlib.pyplot as plt

T = 4
lambd = 2
n = 100
N_t = []
for i in range(n):
    k = poisson.rvs(mu=lambd*T)
    T_prime = np.random.random(k) * T
    T_prime = np.sort(T_prime)

    x_i = [0]
    y_i = [0]

    for i in range(k):
        x_i.append(T_prime[i])
        y_i.append(y_i[-1] + 1)

    N_t.append(max(y_i))

expected_lambda_t = lambd * T
print(range(max(N_t) + 2))
# Sporządzenie histogramu liczby zdarzeń N(t)
plt.hist(N_t, bins=range(max(N_t) + 2), density=True, alpha=0.5, label='Empiryczny')
# Wygenerowanie rozkładu Poissona o oczekiwanej wartości lambda*t
x = np.arange(0, max(N_t) + 1)
poisson_distribution = poisson.pmf(x, mu=expected_lambda_t)
plt.plot(x, poisson_distribution, 'ro-', label='Teoretyczny (Poisson)')
plt.xlabel('Liczba zdarzeń (N(t))')
plt.ylabel('Prawdopodobieństwo')
plt.title('Porównanie empirycznego rozkładu liczby zdarzeń N(t) z rozkładem Poissona')
plt.legend()
plt.show()