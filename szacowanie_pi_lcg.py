import numpy as np
import matplotlib.pyplot as plt
import datetime

ct = datetime.datetime.now()

# zad 1
a = 16807
m = 2**31 - 1
c = 0

# Seed generatora LCG generowany na podstawie czasu
x0 = round(ct.timestamp() * 10 ** 6) % m

v = []
N0 = 200
def LCG(k = 3, x0 = x0, v = [], N = N0, a = 16807, m = 2**31-1, c=0):
    while len(v) < k*N:
        x = (a*x0+c) % m
        v.append(x/m)
        x0 = x
    return(v[::k])

points = []

# Uzyskanie liczb losowych z generatora LCG
x, y = LCG(5)[0::2], LCG(5)[1::2]

# Na podstawie odległości
P = (np.sqrt((np.square(x) + np.square(y))) < 1) / np.size(x)

# wynik * 4, ponieważ spodziewamy się wyniku pi/4
print(P.sum() * 4)
