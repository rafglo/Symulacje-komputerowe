import random
import matplotlib.pyplot as plt
import numpy as np


def ratio_of_uniforms_normal(n):

    x_ = np.linspace(0,1,100)
    y_ = np.sqrt(-2*np.log(x_)*x_**2)
    y__ = - np.sqrt(-2*np.log(x_)*x_**2)

    X = []
    Y = []
    Z = []

    while len(Z) < n: 

        x = random.uniform(0,1)
        y = random.uniform(-1,1)
        
        if 0 <= x:
            if y ** 2 <= -2*np.log(x)*x**2:
                X.append(x)
                Y.append(y)
                Z.append(y/x)
                
    plt.plot(X, Y, '.', color='green')
    plt.plot(x_,y_, color='red')
    plt.plot(x_,y__, color='red')
    plt.show()
    return Z
    
n = 10000
normal_sample = ratio_of_uniforms_normal(n)
