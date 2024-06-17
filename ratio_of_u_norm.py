import random
import matplotlib.pyplot as plt
import numpy as np

def funkcja():
    #parametry to 0, 1
    lista_x = []
    lista_y = []
    while len(lista_x) < 1000:
        x_losowy = random.uniform(0,1)
        y_losowy = random.uniform(-1,1)
        if -2*x_losowy*np.sqrt((-1)*np.log(x_losowy))<y_losowy<2*x_losowy*np.sqrt((-1)*np.log(x_losowy)):
            lista_x.append(x_losowy)
            lista_y.append(y_losowy)
    plt.plot(lista_x,lista_y,'o')
    plt.show()
    arr1 = np.array(lista_x)
    arr2 = np.array(lista_y)
    odp = arr2/arr1
    plt.hist(odp, density = True)
    x = np.linspace(-5, 5, 1000)
    plt.plot(x, 1/np.sqrt(2*np.pi)*np.exp(-1*x**2/2))
    plt.show()
    
funkcja()
