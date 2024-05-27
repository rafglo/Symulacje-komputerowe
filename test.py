import random
import numpy as np
import math
from scipy.special import erfinv
import matplotlib.pyplot as plt
from scipy.stats import norm
import seaborn as sns
n = 255
v = 0.00492867323399
r = 3.6541528853610088 
def ziggurat2(n, r, v, mi, sigma):
    xs = np.zeros(n+1)
    xs[n] = r
    for i in range(n-1,0,-1):
        if -np.log(2*np.pi*(v/xs[i+1]+norm.pdf(xs[i+1], 0, 1))**2) < 0:
            print(i)
        xs[i] = np.sqrt(-np.log((v/xs[i+1]+norm.pdf(xs[i+1], 0, 1))**2))
    run=True
    while run:
        u = np.random.rand(5)
        i = 1 + math.floor(n * u[0])
        x = xs[i] * u[1]
        if np.absolute(x) < xs[i-1]:
            X = x
            run = False
        if i != n:
            y = (norm.pdf(xs[i-1]) - norm.pdf(xs[i])) * u[2]
            if y < norm.pdf(x) - norm.pdf(xs[i]):
                X = x
                run = False
        if np.absolute(x) >= xs[i-1]:
            run2 = True
            while run2:
                d, f = -1 + 2*u[3], u[4]
                x, y = -np.log(np.absolute(d))/3, -np.log(f)
                if 2*y > x**2:
                    if d > 0:
                        X = x + 3
                    else:
                        X = -x - 3
                    run = False
    Y = sigma * X + mi
    return Y

samples = [ziggurat2(n,r,v,0,1) for i in range(100)]
xs = np.linspace(-5,5, 100)
plt.hist(samples, density=True, bins=10)
plt.plot(xs, norm.pdf(xs, 0, 1), label="gęstość teoretyczna")
plt.title("Porównanie unormowanego histogramu z gęstością rozkładu standardowego normalnego")
plt.legend(loc='best')
plt.show()