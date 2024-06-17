import numpy as np
import matplotlib.pyplot as plt

def gamma_process(t, alpha, beta):
    increments = np.random.gamma(alpha * np.diff(t), beta)
    gamma_process = np.cumsum(increments)
    gamma_process = np.insert(gamma_process, 0, 0)
    return gamma_process

def variance_gamma_process(t, theta, sigma, alpha, beta):
    G_t = gamma_process(t, alpha, beta)
    W_Gt = np.random.normal(0, 1, len(G_t) - 1) * np.sqrt(np.diff(G_t))
    W_Gt = np.cumsum(W_Gt)
    W_Gt = np.insert(W_Gt, 0, 0)
    X_t = theta * G_t + sigma * W_Gt
    return X_t

alpha = 1.0
beta = 1.0
theta = 0.1
sigma = 0.2
times = np.linspace(0, 10, 1000)

vg_values = variance_gamma_process(times, theta, sigma, alpha, beta)

plt.figure(figsize=(10, 6))
plt.plot(times, vg_values, drawstyle='steps-post')
plt.xlabel('Czas')
plt.ylabel('Wartość procesu Variance Gamma')
plt.title('Symulacja procesu Variance Gamma')
plt.grid(True)
plt.show()
