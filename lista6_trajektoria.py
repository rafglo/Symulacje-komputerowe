import numpy as np
from scipy.stats import poisson
import matplotlib.pyplot as plt

T = 4
lambd = 2

k = poisson.rvs(mu=lambd*T)
T_prime = np.random.random(k) * T
T_prime = np.sort(T_prime)

x_i = [0]
y_i = [0]

for i in range(k):
    x_i.append(T_prime[i])
    y_i.append(y_i[-1] + 1)

    plt.vlines(x=x_i[-1], ymin=y_i[-1] - 1, ymax=y_i[-1], linestyles='dashed', linewidth=4)
    plt.hlines(y=y_i[-2], xmin=x_i[-2], xmax=x_i[-1], linewidth=4)
    plt.scatter(x=[x_i[-1]], y=[y_i[-2]], facecolors='none', edgecolors='b', s=160)
    plt.scatter(x=[x_i[-1]], y=[y_i[-1]], c='b', s=160)

plt.hlines(y=y_i[-1], xmin=x_i[-1], xmax=T, linewidth=4)

plt.show()

