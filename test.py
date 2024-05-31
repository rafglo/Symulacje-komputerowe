import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

# Parametry rozkładu normalnego
mean = 0
std_dev = 1

# Funkcja gęstości prawdopodobieństwa dla rozkładu normalnego
def normal_pdf(x, mean, std_dev):
    return stats.norm.pdf(x, mean, std_dev)

# Algorytm Zigguratu dla rozkładu normalnego
def ziggurat_normal(mean, std_dev, num_steps):
    r = np.random.random
    u = np.random.uniform

    # Stałe Zigguratu dla rozkładu normalnego
    m1 = 2147483648.0
    vn = 9.91256303526217e-3
    q = 9.91256303526217e-3
    x = np.zeros(num_steps + 1)
    f = np.zeros(num_steps + 1)

    # Initializations
    x[num_steps] = np.sqrt(2.0 * np.exp(1) / q)
    x[0] = 0
    for i in range(1, num_steps):
        x[i] = np.sqrt(-2.0 * np.log(q * x[i-1] / x[num_steps]))
    for i in range(num_steps):
        f[i] = np.exp(-0.5 * x[i] * x[i])

    fall_back_count = 0

    # Generowanie próbek
    while True:
        i = int(r() * num_steps)
        x_candidate = x[i] * u()
        if x_candidate < x[i+1]:
            return x_candidate, fall_back_count
        if i == 0:
            while True:
                x_candidate = -np.log(u()) / x[num_steps]
                y = -np.log(u())
                if y + y > x_candidate * x_candidate:
                    fall_back_count += 1
                    return x_candidate, fall_back_count
        if f[i] + u() * (f[i-1] - f[i]) < np.exp(-0.5 * x_candidate * x_candidate):
            fall_back_count += 1
            return x_candidate, fall_back_count

# Testowanie algorytmu Zigguratu
def test_ziggurat_normal(mean, std_dev, num_steps, num_samples):
    samples = []
    total_fall_back = 0
    
    for _ in range(num_samples):
        sample, fall_back_count = ziggurat_normal(mean, std_dev, num_steps)
        samples.append(sample)
        total_fall_back += fall_back_count
    
    return samples, total_fall_back / num_samples

# Parametry testowe
num_samples = 10000
num_steps_list = [2, 5, 10, 20, 50, 100, 200]

# Testowanie dla różnych liczby schodków
results = []
for num_steps in num_steps_list:
    samples, avg_fall_back = test_ziggurat_normal(mean, std_dev, num_steps, num_samples)
    results.append(avg_fall_back)
    print(f'Liczba schodków: {num_steps}, Średnia liczba nieudanych prób: {avg_fall_back * 100:.2f}%')

# Wykres zależności liczby schodków od % nieudanych prób
plt.plot(num_steps_list, np.array(results) * 100, marker='o')
plt.xlabel('Liczba schodków')
plt.ylabel('% nieudanych prób')
plt.title('Zależność % nieudanych prób od liczby schodków (metoda Zigguratu)')
plt.xscale('log')
plt.grid(True)
plt.show()