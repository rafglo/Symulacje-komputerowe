import random
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

def funkcja(alfa):
    x = np.linspace(0,1,10000)
    y_1 = x
    y_2 = x**((2/alfa)+1)
    lista_x = np.zeros(10000)
    lista_y = np.zeros(10000)
    i = 0
    while i < 10000:
        x_losowy = random.random()
        y_losowy = random.random()
        if 0<=y_losowy<=x_losowy:
            if x_losowy**((2/alfa)+1)<=y_losowy<=x_losowy:
                lista_x[i] = x_losowy
                lista_y[i] = y_losowy
                i += 1
    lista_z = lista_y/lista_x
    plt.plot(lista_x,lista_y,'o')
    plt.plot(x,y_1)
    plt.plot(x,y_2)
    plt.show()

    return lista_z
    
#`funkcja(0.1)

def theo(x, alpha):
    return (alpha+1) *x**alpha

x = np.linspace(0,1,10000)
alpha = 3
    
z_values = funkcja(alpha)
plt.hist(z_values, density=True, bins=50)
plt.plot(x, theo(x,alpha))
plt.show()
