import numpy as np
import matplotlib.pyplot as plt

def generate_poisson_process(lambda_, T):
    # Generowanie czasów oczekiwania
    interarrival_times = np.random.exponential(scale=1/lambda_, size=int(lambda_*T*2))

    # Sumowanie czasów oczekiwania
    times = np.cumsum(interarrival_times)

    # Filtrowanie czasów, aby pozostały tylko te mniejsze niż T
    times = times[times < T]

    return times

def plot_poisson_process(process, T):
    plt.figure(figsize=(10, 5))
    plt.step(process, range(len(process)), where='post', label='Proces Poissona')
    plt.xlabel('Czas')
    plt.ylabel('Liczba zdarzeń')
    plt.title('Trajektoria procesu Poissona na odcinku [0, T]')
    plt.xlim([0, T])
    plt.ylim([0, max(len(process), 1)])
    plt.legend()
    plt.show()

# Parametry
lambda_ = 0.5  # Intensywność procesu Poissona
T = 10  # Długość odcinka czasu

# Generowanie trajektorii procesu Poissona
process = generate_poisson_process(lambda_, T)

# Rysowanie trajektorii
plot_poisson_process(process, T)