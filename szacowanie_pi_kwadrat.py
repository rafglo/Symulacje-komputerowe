import numpy as np

points = []
n = 1000

x = np.linspace(0, 1, n) # tworzy ciąg 0, 1/n, 2/n, ..., i/n, ..., 1
y = x # bo, to kwadrat

x, y = np.meshgrid(x, y)

# Na podstawie odległości
P = (1/n**2) * (np.sqrt((np.square(x) + np.square(y))) < 1)

# wynik * 4, ponieważ spodziewamy się wyniku pi/4
print(P.sum() * 4)
