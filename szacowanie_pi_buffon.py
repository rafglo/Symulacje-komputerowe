import numpy as np
def pi_buffon(l, num_of_points):
    X = [] #miejsca padania środka igły
    alpha = [] #kąty
    num_of_crosses = 0
    for i in range(num_of_points):
        X.append(i/num_of_points) #jednostajne wybieranie miejsca padania igły na osi ox z przedziału [0, 1)
        alpha.append((np.pi/2)*(i/num_of_points)) #jednostajne wybieranie kątów z przedziału [0, pi/2)
    for i in range(num_of_points):
        for j in range(num_of_points):
            a = 0.5 * l * np.cos(alpha[j]) #wyznaczenie dlugości podstawy trójkąta prostokątnego o wierzchołku w p unkcie przecięcia się igły z osią ox o przeciwprostokątnej dlugości l/2.
            if a > X[i] or a > (1 - X[i]): #warunek przecięcia się igły z pasem (z prawej lub lewej strony)
                num_of_crosses += 1
    pi = (2*l)/(num_of_crosses/i**2)
    return pi
