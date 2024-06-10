import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import cauchy

def stable_num_gen(n, alpha, beta):
    sample = np.zeros(n)
    ind = 0
    zeta = 0
    if alpha != 1:
        xi = 1/alpha * np.arctan(-zeta)
    else:
        xi = np.pi/2
    while ind < n:
        u = np.random.uniform(-np.pi/2, np.pi/2)
        w = np.random.exponential(1)
        if alpha != 1:
            x = (1 + zeta**2)**1/(2*alpha)*np.sin(alpha*(u+xi))/np.cos(u)**(1/alpha) * (np.cos(u - alpha*(u+xi)/w))**((1-alpha)/alpha)
        else:
            x = 1/xi * ((np.pi/2 + beta*u)*np.tan(u) - beta * np.log((np.pi/2*w*np.cos(u)/(np.pi/2 + beta*u))))
        sample[ind] = x
        ind += 1
    return sample


n = 10000
alpha = 1
beta = 0
sam = stable_num_gen(n, alpha, beta)
ts = np.linspace(-1000,1000,10000)
ax = plt.gca()
ax.set_xlim([-5, 5])
sns.ecdfplot(sam, label="dystrybuanta empiryczna")
plt.plot(ts, cauchy.cdf(ts), label="dystrybuanta teoretyczna r. Cauchy'ego")
plt.legend(loc="upper left")
plt.title("Porównanie ecdf rozkładu stabilnego z rozkładem Cauchy'ego")
plt.show()