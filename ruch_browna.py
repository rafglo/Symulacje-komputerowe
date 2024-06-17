import numpy as np
import matplotlib.pyplot as plt

def brown_motion_n_dims(dt,T,n):
    Time = np.linspace(0,T,int(np.ceil(T/dt)))
    l = len(Time)
    X = []
    for i in range(n):
        X.append(np.zeros(l))
    
    for N in range(n):    
        for i in range(1,l):
            X[N][i] = X[N][i-1] + np.random.normal(0,dt)
    
    if n == 1:
        plt.title('Brown motion')
        plt.xlabel('time')
        plt.ylabel('value')
        plt.plot(Time,X[0])
        plt.show()
    elif n == 2:
        plt.title('Brown motion')
        plt.xlabel('time')
        plt.ylabel('value')
        plt.plot(X[0], X[1])
        plt.show()
    else:
        return X
