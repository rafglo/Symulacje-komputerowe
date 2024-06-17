import numpy as np
import matplotlib.pyplot as plt
import datetime

def lcg(a, c, m, n, k, x_0):
    x = [x_0]
    for i in range(k*n):
        x.append((x[-1] * a + c) % m)
    y = [i/m for i in x]
    ans = []
    for j in range(0,len(y),k):
        ans.append(y[j])
    return ans

x = lcg(16807, 0, 2**(31) - 1, 1000, 3, round(datetime.datetime.now().timestamp()*10**6)%2**31-1)
y = lcg(16807, 0, 2**(31) - 1, 1000, 3, round(datetime.datetime.now().timestamp()*10**6)%2**31-1)

counter = 0
for i in range(len(x)):
    if np.sqrt(x[i]**2+y[i]**2) <= 1:
        counter += 1
        plt.scatter(x[i],y[i], color = 'green')
    else:
        plt.scatter(x[i],y[i], color = 'red')

wynik = 4*counter/1000


print(wynik)