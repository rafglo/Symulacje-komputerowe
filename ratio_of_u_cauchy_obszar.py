import random
import matplotlib.pyplot as plt
import numpy as np

def ratio_of_uniforms_cauchy(n):

    x_ = np.linspace(0,1,100)
    y_ = np.sqrt(1-x_**2)
    y__ = - np.sqrt(1-x_**2)

    X = []
    Y = []
    Z = []

    while len(Z) < n: 

        x = random.uniform(0,1)
        y = random.uniform(-1,1)
        
        if 0 <= x:
            if 0 <= (x**2 + y**2) <= 1:
                X.append(x)
                Y.append(y)
                Z.append(y/x)

    plt.plot(X, Y, '.', color='green')
    plt.plot(x_,y_, color='red')
    plt.plot(x_,y__, color='red')
    plt.show()
    return Z
    
n = 1000
cauchy_sample = ratio_of_uniforms_cauchy(n)
