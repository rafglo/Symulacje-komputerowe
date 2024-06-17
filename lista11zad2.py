import numpy as np
import matplotlib.pyplot as plt

def RuchBrowna(t,dt,n=1):
    T = np.arange(0,t,dt)
    S = [[np.random.normal(0,1,len(T))*np.sqrt(dt)] for j in range(n)]
    S = [np.cumsum(i) for i in S]
    return S

def MSE(t):
    MSE = (np.sum((t-np.mean(t))**2))/len(t)
    return MSE

B = RuchBrowna(100,0.001,100)
B = np.transpose(B)

Ms = [MSE(c) for c in B]
plt.plot(np.arange(0,100,0.001),Ms)
plt.plot(np.arange(0,100))
plt.show()