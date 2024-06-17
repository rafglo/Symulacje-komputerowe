import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

N = 10000
dt = 0.01

np.random.seed(0)  # Ustawienie ziarna dla powtarzalności

lower_limit = -1
upper_limit = 1

first_exit_times = np.zeros(N)

for i in range(N):
    w0 = 0
    k0 = 0
    t = 0

    wi = w0
    ki = k0

    while (wi >= lower_limit and wi <= upper_limit and ki >= lower_limit and ki <= upper_limit):
        dW = np.random.normal(0, 1) * np.sqrt(dt)
        dK = np.random.normal(0, 1) * np.sqrt(dt)
        wi += dW
        ki +=dK
        t += dt
    
    first_exit_times[i] = t

sns.histplot(first_exit_times, stat="density", color='g', bins=30)
plt.title('Histogram pierwszego czasu wyjścia')
plt.show()
