import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson

def generate_poisson_process(lambda_, T, num_trajectories):
    # Inicjalizacja listy przechowującej liczby zdarzeń N(t) dla każdej trajektorii
    Nt_values = []

    for _ in range(num_trajectories):
        # Generowanie czasów między kolejnymi zdarzeniami
        interarrival_times = np.random.exponential(scale=1/lambda_, size=int(lambda_*T*2))
        # Sumowanie czasów oczekiwania
        times = np.cumsum(interarrival_times)
        # Filtrowanie czasów, aby pozostały tylko te mniejsze niż T
        times = times[times < T]
        # Obliczanie N(t)
        Nt = len(times)
        # Dodanie N(t) do listy
        Nt_values.append(Nt)

    return Nt_values

# Parametry
lambda_ = 0.5  # Intensywność procesu Poissona
T = 10  # Długość odcinka czasu
num_trajectories = 1000  # Liczba trajektorii

# Generowanie trajektorii procesu Poissona
Nt_values = generate_poisson_process(lambda_, T, num_trajectories)

# Oczekiwana wartość N(t)
expected_lambda_t = lambda_ * T

# Sporządzenie histogramu liczby zdarzeń N(t)
plt.hist(Nt_values, bins=range(max(Nt_values) + 2), density=True, alpha=0.5, label='Empiryczny')
# Wygenerowanie rozkładu Poissona o oczekiwanej wartości lambda*t
x = np.arange(0, max(Nt_values) + 1)
poisson_distribution = poisson.pmf(x, mu=expected_lambda_t)
plt.plot(x, poisson_distribution, 'ro-', label='Teoretyczny (Poisson)')
plt.xlabel('Liczba zdarzeń (N(t))')
plt.ylabel('Prawdopodobieństwo')
plt.title('Porównanie empirycznego rozkładu liczby zdarzeń N(t) z rozkładem Poissona')
plt.legend()
plt.show()